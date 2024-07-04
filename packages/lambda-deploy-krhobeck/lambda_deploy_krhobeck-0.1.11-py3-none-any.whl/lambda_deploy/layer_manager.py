import json
import os
import shutil
import subprocess
import sys
from typing import List
from boto3 import Session
from boto3.exceptions import Boto3Error
from mypy_boto3_lambda.client import LambdaClient


def create_temp_directory(source_path: str, base_path: str) -> None:
    """Create a temporary directory for building the layer."""
    full_path = os.path.join(source_path, base_path)
    if os.path.exists(full_path):
        shutil.rmtree(full_path)
    os.makedirs(full_path)


def setup_directory_structure(source_path: str, base_path: str) -> str:
    """Set up the directory structure for Python packages within the layer."""
    python_lib_path = os.path.join(
        source_path, base_path, "python", "lib", "python3.10", "site-packages"
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


def read_manifest(lib_path: str) -> set:
    """Read the current manifest of installed packages."""
    try:
        with open(f"{lib_path}/manifest.json", "r") as f:
            manifest = json.load(f)
        return set(manifest)
    except FileNotFoundError:
        return set()


def write_manifest(lib_path: str, packages: List[str]):
    """Write the current list of packages to the manifest."""
    with open(f"{lib_path}/manifest.json", "w") as f:
        json.dump(packages, f)


def install_external_packages(packages: List[str], lib_path: str):
    """Install external packages into the specified library path."""
    current_packages = set(packages)
    installed_packages = read_manifest(lib_path)

    if current_packages != installed_packages:
        print(f"Installing external packages into {lib_path}")
        for package in packages:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    package,
                    "-t",
                    lib_path,
                ],
                check=True,
            )
        write_manifest(lib_path, packages)
    else:
        print("No installation needed; packages are up-to-date.")


def zip_layer(source_path: str, base_dir: str, zip_name: str) -> str:
    """Zip the layer directory."""
    full_zip_path = os.path.join(source_path, zip_name)
    shutil.make_archive(
        base_name=full_zip_path.replace(".zip", ""),
        format="zip",
        root_dir=os.path.join(source_path, base_dir),
    )
    return full_zip_path


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
    source_path: str,
    layer_name: str,
    layer_dirs: List[str],
    external_packages: List[str],
    session: Session,
):
    """
    Sets up layers.
    """
    base_path = "lambda_layer"
    zip_path = "lambda_layer.zip"
    create_temp_directory(source_path, base_path)
    python_lib_path = setup_directory_structure(source_path, base_path)
    if layer_dirs:
        copy_directories_to_build(layer_dirs, python_lib_path)
    if external_packages:
        install_external_packages(external_packages, python_lib_path)
    zip_layer(source_path, base_path, zip_path)
    upload_layer(session, os.path.join(source_path, zip_path), layer_name)
