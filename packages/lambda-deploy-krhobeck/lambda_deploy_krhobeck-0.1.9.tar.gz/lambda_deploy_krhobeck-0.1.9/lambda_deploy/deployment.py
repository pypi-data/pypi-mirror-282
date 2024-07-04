import boto3
import logging
from boto3 import Session
from lambda_deploy.api_gateway_manager import setup_api_gateway
from lambda_deploy.lambda_manager import setup_lambdas
from lambda_deploy.layer_manager import setup_layers
from lambda_deploy.s3_manager import check_s3_exists
from mypy_boto3_s3.client import S3Client


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_session() -> Session:
    return boto3.Session()


def check_connection(session: Session) -> None:
    s3: S3Client = session.client("s3")
    try:
        s3.list_buckets()
    except Exception as e:
        print(f"Failed to connect to AWS: {str(e)}")
        raise


def deploy(
    source_path: str,
    bucket_name: str,
    layer_name: str,
    user_pool_id: str,
    domain_name: str,
    certificate_arn: str,
    layer_directories=None,
    external_packages=None,
) -> None:
    """
    Deploys all lambda functions and layers, sets up API Gateway,
    and configures IAM roles and permissions.
    :return:
    """
    logging.info("Starting deployment process.")
    logging.info("Creating a new boto3 session.")
    boto3_session: Session = get_session()
    logging.info("Checking connection to AWS services.")
    check_connection(boto3_session)
    logging.info("Checking existence of S3 bucket.")
    check_s3_exists(boto3_session, bucket_name=bucket_name)
    if layer_directories or external_packages:
        logging.info(
            "Setting up Lambda layers with provided directories and packages."
        )
        setup_layers(
            source_path,
            layer_name,
            layer_directories,
            external_packages,
            boto3_session,
        )
    logging.info("Aggregating lambda function configurations.")
    logging.info("Setting up lambda functions.")
    setup_lambdas(boto3_session)
    logging.info("Setting up API Gateway.")
    setup_api_gateway(
        boto3_session, user_pool_id, domain_name, certificate_arn
    )
    logging.info("Deployment process completed successfully.")
