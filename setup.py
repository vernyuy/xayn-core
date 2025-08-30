from setuptools import setup, find_packages

setup(
    name="aws-helpers",
    version="0.1.0",
    description="Helper library for AWS DynamoDB and S3 operations",
    author="Fonchu",
    author_email="fonchu.e.venyuy@gmail.com",
    packages=find_packages(),
    install_requires=[
        "boto3"
    ],
    python_requires=">=3.8",
)
