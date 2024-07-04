import boto3
from boto3 import Session
from mypy_boto3_apigateway.client import APIGatewayClient
from decorators import (
    lambda_functions,
)


def create_rest_api(api_gateway: APIGatewayClient, api_name: str):
    """Create a new REST API and return its details."""
    response = api_gateway.create_rest_api(name=api_name)
    return response["id"]


def get_root_resource_id(api_gateway: APIGatewayClient, api_id: str):
    """Retrieve the root resource ID for the given API."""
    response = api_gateway.get_resources(restApiId=api_id)
    for item in response["items"]:
        if item["path"] == "/":
            return item["id"]
    return None


def create_resource(
    api_gateway: APIGatewayClient, api_id: str, parent_id: str, path_part: str
):
    """Create a resource within the REST API."""
    response = api_gateway.create_resource(
        restApiId=api_id, parentId=parent_id, pathPart=path_part
    )
    return response["id"]


def setup_method(
    api_gateway: APIGatewayClient,
    api_id: str,
    resource_id: str,
    lambda_function_data,
):
    """Setup a method for a resource, with optional CORS and authorizer."""
    http_method = lambda_function_data["http_method"]
    cors_config = lambda_function_data.get("cors_config")
    authorizer_config = lambda_function_data.get("authorizer")

    # Setup method with potential authorizer
    authorization_type = "NONE" if not authorizer_config else "CUSTOM"
    authorizer_id = authorizer_config.authorizer_id
    api_gateway.put_method(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=http_method,
        authorizationType=authorization_type,
        authorizerId=authorizer_id,
    )

    # Setup integration with AWS Lambda
    uri = (
        f"arn:aws:apigateway:{boto3.Session().region_name}:lambda:path"
        f"/2015-03-31/functions/{lambda_function_data['lambda_arn']}"
        f"/invocations"
    )
    api_gateway.put_integration(
        restApiId=api_id,
        resourceId=resource_id,
        httpMethod=http_method,
        type="AWS_PROXY",
        integrationHttpMethod="POST",
        uri=uri,
    )

    # Setup CORS if configured
    if cors_config:
        allow_origin = "method.response.header.Access-Control-Allow-Origin"
        allow_headers = "method.response.header.Access-Control-Allow-Headers"
        allow_methods = "method.response.header.Access-Control-Allow-Methods"
        api_gateway.put_method_response(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod=http_method,
            statusCode="200",
            responseParameters={
                allow_origin: True,
                allow_headers: True,
                allow_methods: True,
            },
        )
        integration_resp_parameters = {
            allow_origin: f"'{cors_config.allowed_origin}'",
            allow_headers: f"'{cors_config.allowed_headers}'",
            allow_methods: f"'{cors_config.allowed_methods}'",
        }
        api_gateway.put_integration_response(
            restApiId=api_id,
            resourceId=resource_id,
            httpMethod=http_method,
            statusCode="200",
            responseParameters=integration_resp_parameters,
        )


def deploy_api(api_gateway: APIGatewayClient, api_id: str, stage_name: str):
    """Deploy the API to make it available to clients."""
    api_gateway.create_deployment(restApiId=api_id, stageName=stage_name)


def setup_api_gateway(session: Session):
    """Setup API Gateway based on configured lambda functions."""
    api_gateway: APIGatewayClient = session.client("apigateway")
    for func_data in lambda_functions:
        api_name = f"{func_data['name']} API"
        api_id = create_rest_api(api_gateway, api_name)
        root_id = get_root_resource_id(api_gateway, api_id)
        resource_id = create_resource(
            api_gateway, api_id, root_id, func_data["endpoint"]
        )

        setup_method(api_gateway, api_id, resource_id, func_data)
        deploy_api(api_gateway, api_id, "Dev")
