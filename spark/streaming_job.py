import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

# Parse arguments for dynamic paths
parser = argparse.ArgumentParser()
parser.add_argument("--checkpoint", required=True, help="Checkpoint directory")
parser.add_argument("--output", required=True, help="Output directory for Parquet")
args = parser.parse_args()

# Initialize Spark session
spark = SparkSession.builder.appName("SmartCityStreaming").getOrCreate()

# Define schema for incoming IoT sensor data
schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("timestamp", StringType()),
    StructField("temperature", DoubleType()),
    StructField("co2", IntegerType()),
    StructField("traffic", IntegerType())
])

# Create streaming DataFrame by reading from Kafka topic
df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "smartcity.iot")
    .load()
)

# Parse JSON data from Kafka messages and extract fields
parsed = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Write processed stream to Parquet files with dynamic paths
query = (
    parsed.writeStream
    .format("parquet")
    .option("path", args.output)
    .option("checkpointLocation", args.checkpoint)
    .outputMode("append")
    .trigger(processingTime="30 seconds")
    .start()
)

query.awaitTermination(60)  # run for 60 seconds then exit
