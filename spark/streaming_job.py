import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

# Parse arguments for dynamic paths
parser = argparse.ArgumentParser()
parser.add_argument("--checkpoint", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

# Initialize Spark session
spark = SparkSession.builder.appName("SmartCityStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Define schema
schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("timestamp", StringType()),
    StructField("temperature", DoubleType()),
    StructField("co2", IntegerType()),
    StructField("traffic", IntegerType())
])

# Read from Kafka in BATCH mode
df = (
    spark.read                                          # ← Batch read
    .format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "smartcity.iot")
    .option("startingOffsets", "earliest")             # ← Lire depuis le début
    .option("endingOffsets", "latest")                 # ← Jusqu'au dernier message
    .load()
)

# Parse JSON
parsed = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Filter dummy records
parsed = parsed.filter(col("sensor_id") != "DUMMY-INIT")

# Write to Parquet in BATCH mode
parsed.write \                                         # ← Batch write
    .format("parquet") \
    .mode("append") \
    .save(args.output)

print(f"✅ Data written to {args.output}")
print(f"✅ Total records: {parsed.count()}")

spark.stop()