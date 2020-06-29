#!/usr/bin/env python3

from aws_cdk import core

from lambda_bundler_demo.lambda_bundler_demo_stack import LambdaBundlerDemoStack


app = core.App()
LambdaBundlerDemoStack(app, "lambda-bundler-demo")

app.synth()
