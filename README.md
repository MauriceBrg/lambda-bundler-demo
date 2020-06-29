# Lambda Bundler Demo

![Lambda-Bundler-Demo-Build](https://github.com/MauriceBrg/lambda-bundler-demo/workflows/Lambda-Bundler-Demo-Build/badge.svg)

This project is a demo of the `lambda-bundler` python library, which allows you to package your python lambda functions and their dependencies using pure python.

You can find the repo [here on Github](https://github.com/MauriceBrg/lambda_bundler) and the package [here on PyPi](https://pypi.org/project/lambda-bundler/).

## About this demo

This demo is an AWS Cloud Development Kit (CDK) app that deploys three lambda functions:

1. A lambda function without external dependencies
2. A lambda function with small external dependencies
3. A lambda function with large external dependencies that are deployed in a layer

You can have a look at the code in `lambda_bundler_demo/lambda_bundler_demo_stack.py` and see how it's done.
