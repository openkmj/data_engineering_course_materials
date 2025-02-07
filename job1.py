from pyspark.sql import SparkSession

# Spark 세션 생성
spark = SparkSession.builder.appName("RowCountJob").getOrCreate()

# S3에서 Parquet 파일 읽기
s3_input_path = "s3://de-team3-test-bucket/input-data/"
df = spark.read.parquet(s3_input_path)

# Row count 계산
row_count = df.count()

# 결과를 DataFrame으로 변환
result_df = spark.createDataFrame([(row_count,)], ["row_count"])

# S3에 CSV로 저장
s3_output_path = "s3://de-team3-test-bucket/output-data/result.csv"
result_df.write.mode("overwrite").csv(s3_output_path, header=True)

spark.stop()
