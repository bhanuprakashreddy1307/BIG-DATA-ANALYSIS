from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, sum
import random

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("LargeDatasetAnalysis") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()


# Generate Sample Data (Simulating a Large Dataset)
data = [(i, random.randint(18, 65), random.choice(["M", "F"]), random.randint(1000, 50000)) for i in rage(1, 1000001)]

# Define Schema
columns = ["ID", "Age", "Gender", "Salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Display Schema and Sample Data
df.printSchema()
df.show(5)

# Perform Aggregations
agg_result = df.groupBy("Gender").agg(
    count("*").alias("Count"),
    avg("Age").alias("Average_Age"),
    avg("Salary").alias("Average_Salary"),
    sum("Salary").alias("Total_Salary")
)

# Show Aggregated Results
agg_result.show()

# Stop Spark Session
spark.stop()
