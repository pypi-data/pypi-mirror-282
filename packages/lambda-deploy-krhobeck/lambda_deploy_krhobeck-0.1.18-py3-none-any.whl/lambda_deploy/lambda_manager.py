import json
from typing import Dict, Any

from boto3 import Session
from mypy_boto3_iam.client import IAMClient
from mypy_boto3_lambda.client import LambdaClient
from mypy_boto3_s3.client import S3Client
from lambda_deploy.decorators import lambda_functions


def get_account_id(session):
    """Retrieve the account ID using an AWS STS client."""
    sts_client = session.client("sts")
    identity = sts_client.get_caller_identity()
    return identity["Account"]


def upload_lambda_code(
    session: Session, lambda_function_data: object, source_path: str
):
    """Uploads lambda function code to an S3 bucket."""
    s3: S3Client = session.client("s3")
    function_path = (
        source_path + lambda_function_data._lambda_meta["file_path"]
    )
    print("function path is", function_path)
    s3.upload_fileobj(
        Fileobj=open(function_path, "rb"),
        Bucket=lambda_function_data._lambda_meta["s3_bucket"],
        Key=lambda_function_data._lambda_meta["s3_key"],
    )


def create_iam_policy_document(session, permissions):
    """Generate an IAM policy document from permissions."""
    account_id = get_account_id(session)
    region = session.region_name
    statements = []

    for perm in permissions:
        resource_type = perm["resource_type"].lower()
        actions = perm.get("actions")
        if resource_type == "s3":
            resource = [
                f"arn:aws:s3:::{perm['resource_name']}",
                f"arn:aws:s3:::{perm['resource_name']}/*",
            ]
        elif resource_type == "dynamodb":
            resource = [
                f"arn:aws:dynamodb:{region}:{account_id}:table/"
                f"{perm['resource_name']}"
            ]
        elif resource_type == "cognito":
            resource = [
                f"arn:aws:cognito-idp:{region}:{account_id}:userpool/"
                f"{perm['resource_name']}"
            ]
        else:
            resource = [
                f"arn:aws:{resource_type}:{region}:{account_id}:"
                f"{perm['resource_name']}"
            ]

        statements.append(
            {"Effect": "Allow", "Action": actions, "Resource": resource}
        )

    return {"Version": "2012-10-17", "Statement": statements}


def create_or_update_lambda_role(session: Session, role_name: str, iam_config):
    """Ensure the IAM role for Lambda exists and attach policies."""
    iam: IAMClient = session.client("iam")
    policy_document = create_iam_policy_document(
        session, iam_config["permissions"]
    )
    try:
        role = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {"Service": "lambda.amazonaws.com"},
                            "Action": "sts:AssumeRole",
                        }
                    ],
                }
            ),
            Description="Lambda execution role",
        )
        role_arn = role["Role"]["Arn"]
    except iam.exceptions.EntityAlreadyExistsException:
        role_arn = iam.get_role(RoleName=role_name)["Role"]["Arn"]

    policy_name = f"{role_name}-policy"
    policy = iam.create_policy(
        PolicyName=policy_name, PolicyDocument=json.dumps(policy_document)
    )
    iam.attach_role_policy(
        RoleName=role_name, PolicyArn=policy["Policy"]["Arn"]
    )
    return role_arn


def setup_lambdas(session: Session, source_path: str):
    """Setup Lambda functions based on metadata from decorators."""
    print("Lambdas are", lambda_functions)
    for lambda_function_data in lambda_functions:
        upload_lambda_code(session, lambda_function_data, source_path)
        role_arn = create_or_update_lambda_role(
            session,
            lambda_function_data["role_name"],
            lambda_function_data["iam_config"],
        )
        lambda_client: LambdaClient = session.client("lambda")
        lambda_client.create_function(
            FunctionName=lambda_function_data["name"],
            Runtime=lambda_function_data["runtime"],
            Role=role_arn,
            Handler=lambda_function_data["handler"],
            Code={
                "S3Bucket": lambda_function_data["s3_bucket"],
                "S3Key": lambda_function_data["s3_key"],
            },
            Description=lambda_function_data.get(
                "description", "Deployed via automated system"
            ),
            Timeout=lambda_function_data.get("timeout", 500),
            MemorySize=lambda_function_data.get("memory_size", 128),
            Publish=True,
        )
