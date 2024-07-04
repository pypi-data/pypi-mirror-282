import os
import shutil
import subprocess
import sys
from typing import List
from boto3 import Session
from boto3.exceptions import Boto3Error
from mypy_boto3_lambda.client import LambdaClient


def create_temp_directory(base_path: str) -> None:
    """Create a temporary directory for building the layer."""
    if os.path.exists(base_path):
        shutil.rmtree(base_path)
    os.makedirs(base_path)


def setup_directory_structure(base_path: str) -> str:
    """Set up the directory structure for Python packages within the layer."""
    python_lib_path = os.path.join(
        base_path, "python", "lib", "python3.10", "site-packages"
    )
    os.makedirs(python_lib_path)
    return python_lib_path


def copy_directories_to_build(layer_dirs: List[str], target_path: str):
    """Copy each specified directory to the build directory."""
    for dir_path in layer_dirs:
        if os.path.exists(dir_path):
            shutil.copytree(
                dir_path, os.path.join(target_path, os.path.basename(dir_path))
            )


def install_external_packages(packages: List[str], lib_path: str):
    """Install external packages into the specified library path."""
    for package in packages:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", package, "-t", lib_path],
            check=True,
        )


def zip_layer(source_dir: str, zip_path: str) -> str:
    """Zip the layer directory."""
    shutil.make_archive(
        base_name=zip_path.replace(".zip", ""),
        format="zip",
        root_dir=source_dir,
    )
    return zip_path


def upload_layer(
    session: Session,
    zip_path: str,
    layer_name: str,
) -> None:
    """Upload the zipped layer to AWS Lambda."""
    lambda_client: LambdaClient = session.client("lambda")
    with open(zip_path, "rb") as layer_zip:
        try:
            lambda_client.publish_layer_version(
                LayerName=layer_name,
                Description="Layer with custom Python packages and libraries",
                Content={"ZipFile": layer_zip.read()},
                CompatibleRuntimes=["python3.10"],
            )
        except Boto3Error as e:
            raise e


def setup_layers(
    layer_name: str,
    layer_dirs: List[str],
    external_packages: List[str],
    session: Session,
):
    """
    Sets up layers
    :param layer_name:
    :param layer_dirs:
    :param external_packages:
    :param session:
    :return:
    """
    base_path = "/tmp/lambda_layer"
    zip_path = "/tmp/lambda_layer.zip"
    create_temp_directory(base_path)
    python_lib_path = setup_directory_structure(base_path)
    if layer_dirs:
        copy_directories_to_build(layer_dirs, python_lib_path)
    if external_packages:
        install_external_packages(external_packages, python_lib_path)
    zipped_path = zip_layer(base_path, zip_path)
    upload_layer(session, zipped_path, layer_name)
