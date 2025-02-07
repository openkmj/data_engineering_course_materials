import json
import boto3
import pandas as pd

BUCKET_NAME = "de-team3-test-bucket"
OBJECT_KEY = "yellow_tripdata_2024-01.parquet"


def lambda_handler(event, context):
    # get parquet file from s3
    s3_client = boto3.client("s3")

    # read parquet file
    df = pd.read_parquet(f"s3://{BUCKET_NAME}/{OBJECT_KEY}")

    # filter by pickup_datetime
    # df = df[df["pickup_datetime"] == "2024-01-01"]
    print(df.count())


lambda_handler()
