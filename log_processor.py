from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("LogProcessing").getOrCreate()

# Read logs from Kafka
logs_df = spark.readStream.format("kafka").option("subscribe", "logs_topic").load()

# Process logs to detect anomalies
processed_df = logs_df.withColumn("anomaly", when(col("level") == "ERROR", 1).otherwise(0))

# Write processed logs to Snowflake
processed_df.write.format("snowflake").option("dbtable", "processed_logs").save()
