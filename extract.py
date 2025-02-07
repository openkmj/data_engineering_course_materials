import boto3
import requests

TARGET_URL = (
    "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
)

BUCKET_NAME = "de-team3-test-bucket"

OBJECT_KEY = "yellow_tripdata_2024-01.parquet"

response = requests.get(TARGET_URL, stream=True)

s3_client = boto3.client("s3")

s3_client.upload_fileobj(response.raw, BUCKET_NAME, OBJECT_KEY)
