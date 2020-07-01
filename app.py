#!/usr/bin/env python3
import logging
import sys
from aws_cdk import core

from lambda_bundler_demo.lambda_bundler_demo_stack import LambdaBundlerDemoStack

LOGGER = logging.getLogger("lambda_bundler")
LOGGER.setLevel(logging.DEBUG)

def configure_logging() -> None:
    """
    Sets up the logging configuration for the CDK app.
    :return: Nothing.
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s -  %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)


configure_logging()
app = core.App()
LambdaBundlerDemoStack(app, "lambda-bundler-demo")

app.synth()
