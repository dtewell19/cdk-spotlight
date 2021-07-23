from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications,
    core
)


class LambdaFunctionStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, s3_bucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # import existing s3 bucket
        s3 = _s3.Bucket.from_bucket_arn(self, "s3_bucket", bucket_arn=s3_bucket.bucket_arn)

        #create lambda layer
        layer = _lambda.LayerVersion(self, "lambda_layer",
            code=_lambda.Code.from_asset("./layer_code"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_8],
            license="Apache-2.0",
            description="A layer to test the L2 construct"
        )

        # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_8,
                                    handler="lambda-handler.main",
                                    code=_lambda.Code.asset("./lambda_code"),
                                    layers=[layer]
                                    )

        # add permission for lambda to read from s3
        s3.grant_read(function)

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
