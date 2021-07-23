#!/usr/bin/env python3

from aws_cdk import core

from s3_bucket.s3trigger_stack import S3TriggerStack
from lambda_func.lambda_func_stack import LambdaFunctionStack

app = core.App()

s3_stack = S3TriggerStack(
    app,
    "s3-bucket"
)

lambda_stack = LambdaFunctionStack(
    app,
    "lambda-func",
    s3_bucket=s3_stack.s3
)

app.synth()
