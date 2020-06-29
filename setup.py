import os
import setuptools


with open("README.md") as fp:
    long_description = fp.read()

CDK_VERSION = os.environ.get("CDK_VERSION", "1.46.0")

setuptools.setup(
    name="lambda_bundler_demo",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "lambda_bundler_demo"},
    packages=setuptools.find_packages(where="lambda_bundler_demo"),

    install_requires=[
        f"aws-cdk.aws-lambda=={CDK_VERSION}",
        f"aws-cdk.core=={CDK_VERSION}",
        "lambda-bundler"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
