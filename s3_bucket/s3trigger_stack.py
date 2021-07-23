from aws_cdk import (
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications,
    core
)


class S3TriggerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create s3 bucket
        self.s3 = _s3.Bucket(
            self, 
            "s3bucket",
    )
