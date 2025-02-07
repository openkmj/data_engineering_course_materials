import argparse

from pyspark.sql import SparkSession


def transform_data(data_source, output_uri):
    """
    Processes sample food establishment inspection data and queries the data to find the top 10 establishments
    with the most Red violations from 2006 to 2020.

    :param data_source: The URI of your food establishment data CSV, such as 's3://amzn-s3-demo-bucket/food-establishment-data.csv'.
    :param output_uri: The URI where output is written, such as 's3://amzn-s3-demo-bucket/restaurant_violation_results'.
    """
    with SparkSession.builder.appName("Transform Data").getOrCreate() as spark:
        # read parquet
        if data_source is not None:
            df = spark.read.parquet(data_source)

        df = df.dropna(
            subset=[
                "tpep_pickup_datetime",
                "tpep_dropoff_datetime",
                "passenger_count",
                "trip_distance",
            ]
        )
        df = df.filter(df.fare_amount > 0)
        df = df.filter(df.trip_distance > 0)

        # sort with trip_distance
        df = df.orderBy(df.trip_distance.desc())

        # write to parquet
        df.write.mode("overwrite").parquet(output_uri)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_source",
        help="The URI for you parquet data, like an S3 bucket location.",
    )
    parser.add_argument(
        "--output_uri",
        help="The URI where output is saved, like an S3 bucket location.",
    )
    args = parser.parse_args()

    transform_data(args.data_source, args.output_uri)

# aws emr add-steps --cluster-id j-33XGB2Q0STB27 --steps "Type=Spark,Name=TEST2,ActionOnFailure=CONTINUE,Args=[s3://de-team3-test-bucket/job2.py,--data_source,s3://de-team3-test-bucket/yellow/2024-01.parquet,--output_uri,s3://de-team3-test-bucket/out2]"
