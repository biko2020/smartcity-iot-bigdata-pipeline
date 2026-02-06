from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import *

# Initialize Spark session for streaming application
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

# Write processed stream to Parquet files
parsed.writeStream \
    .format("parquet") \                                      
    .option("path", "/app/data/processed/smartcity") \        
    .option("checkpointLocation", "/app/checkpoints") \       
    .outputMode("append") \                                  
    .start() \                                                
    .awaitTermination()                                      