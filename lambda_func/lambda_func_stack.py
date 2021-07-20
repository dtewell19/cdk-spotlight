from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications,
    core
)


class LambdaFunctionStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, s3_bucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3 = _s3.Bucket.from_bucket_arn(self, "s3_bucket", bucket_arn=s3_bucket.bucket_arn)

        # create lambda function
        function = _lambda.Function(self, "lambda_function",
                                    runtime=_lambda.Runtime.PYTHON_3_7,
                                    handler="lambda-handler.main",
                                    code=_lambda.Code.asset("./lambda"))

        # add permission for lambda to read from s3
        s3.grant_read(function)

        # create s3 notification for lambda function
        notification = aws_s3_notifications.LambdaDestination(function)

        # assign notification for the s3 event type (ex: OBJECT_CREATED)
        s3.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
