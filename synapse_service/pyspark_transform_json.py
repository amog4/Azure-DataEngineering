from os import sched_rr_get_interval
from pyspark.sql import SparkSession
from pyspark.sql.type import *



spark = SparkSession \
    .builder \
    .appName("Python Spark SQL") \
    .getOrCreate()

df = spark.read.json('')

schema = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), False)])
