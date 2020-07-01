import os
import logging

from aws_cdk import aws_lambda as _lambda
from aws_cdk import core

from lambda_bundler import build_layer_package, build_lambda_package

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

def get_project_root() -> str:
    """Returns the path to the project's root directory.

    :return: Path to the project's root directory.
    :rtype: str
    """
    return os.path.join(os.path.dirname(__file__), "..")

class LambdaBundlerDemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        LOGGER.info("Building small lambda package...")

        # Small Lambda without external dependencies
        path_to_small_package = build_lambda_package(
            code_directories=[
                os.path.join(get_project_root(), "src")
            ]
        )
        LOGGER.info("Path to small package: %s", path_to_small_package)

        small_lambda = _lambda.Function(
            self,
            "small-function",
            code=_lambda.Code.from_asset(path=path_to_small_package),
            handler="src.functions.small.handler.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_7
        )

        LOGGER.info("Building medium lambda package...")
        # Medium Lambda with lightweight external dependencies
        path_to_medium_package = build_lambda_package(
            code_directories=[
                os.path.join(get_project_root(), "src")
            ],
            requirement_files=[
                os.path.join(get_project_root(), "src", "functions", "medium", "requirements.txt")
            ]
        )
        LOGGER.info("Path to medium package: %s", path_to_medium_package)

        medium_lambda = _lambda.Function(
            self,
            "medium-function",
            code=_lambda.Code.from_asset(path=path_to_medium_package),
            handler="src.functions.medium.handler.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_7
        )

        LOGGER.info("Building large lambda package...")
        # Large Lambda with Heavy external dependencies that require a lambda layer.
        path_to_large_package = build_lambda_package(
            code_directories=[
                os.path.join(get_project_root(), "src")
            ]
        )
        LOGGER.info("Path to large package: %s", path_to_large_package)

        LOGGER.info("Building lambda layer package...")
        path_to_layer_package = build_layer_package(
            requirement_files=[
                os.path.join(get_project_root(), "src", "functions", "large", "requirements.txt")
            ]
        )
        LOGGER.info("Path to layer package: %s", path_to_layer_package)

        # The code that defines your stack goes here
        large_lambda = _lambda.Function(
            self,
            "large-function",
            code=_lambda.Code.from_asset(path=path_to_large_package),
            handler="src.functions.large.handler.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_7,
            layers=[
                _lambda.LayerVersion(
                    self,
                    "large-layer",
                    code=_lambda.Code.from_asset(path=path_to_layer_package),
                    compatible_runtimes=[_lambda.Runtime.PYTHON_3_7]
                )
            ]
        )
