from diagrams import Diagram, Node
from diagrams.aws.network import APIGateway
from diagrams.aws.compute import Lambda
from diagrams.aws.analytics import KinesisDataFirehose
from diagrams.aws.storage import S3
from diagrams.saas.analytics import Snowflake
from diagrams.programming.language import Python
from diagrams.onprem.client import Client



with Diagram("ETL - SCD1 using Snowflake Tasks, Streams & Stored Procedure", show=False, filename="diagrams/architecture", outformat="png"):
    # api = APIGateway("API Gateway")
    # lam = Lambda("Lambda Processor")
    # firehose = KinesisDataFirehose("Firehose")
    s3 = S3("S3 Bucket")
    # s3error = S3("Error Logs")
    snowflake = Snowflake("Snowflake Table")
    stream = Snowflake("Stream")
    task = Snowflake("Task")
    sp = Snowflake("StoredProc")
    python = Python("Anaconda Python")
    csv = Client("Local .csv file")

    csv >> python >> s3 >> stream >> task >> sp >> snowflake
