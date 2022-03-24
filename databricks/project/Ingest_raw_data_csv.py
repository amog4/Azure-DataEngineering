# Databricks notebook source
# MAGIC %fs

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

# MAGIC %fs
# MAGIC ls dbfs:/mnt/test3434vgg/raw/

# COMMAND ----------

df = spark.read.csv('dbfs:/mnt/test3434vgg/raw/circuits.csv',header=True,inferSchema =True)

# COMMAND ----------

df

# COMMAND ----------

display(df.head(5))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

circuits_schema = StructType(fields=[StructField("circuitId", IntegerType(), False),
                                     StructField("circuitRef", StringType(), True),
                                     StructField("name", StringType(), True),
                                     StructField("location", StringType(), True),
                                     StructField("country", StringType(), True),
                                     StructField("lat", DoubleType(), True),
                                     StructField("lng", DoubleType(), True),
                                     StructField("alt", IntegerType(), True),
                                     StructField("url", StringType(), True)
])

# COMMAND ----------

df = spark.read.csv('dbfs:/mnt/test3434vgg/raw/circuits.csv',header=True,schema =circuits_schema )

# COMMAND ----------

from pyspark.sql.functions import col,lit,current_timestamp

# COMMAND ----------

circuits_selected_df = df.select(col("circuitId"), col("circuitRef"), col("name"), col("location"), col("country"), col("lat"), col("lng"), col("alt"))

# COMMAND ----------

circuits_renamed_df = circuits_selected_df.withColumnRenamed("circuitId", "circuit_id") \
.withColumnRenamed("circuitRef", "circuit_ref") \
.withColumnRenamed("lat", "latitude") \
.withColumnRenamed("lng", "longitude") \
.withColumnRenamed("alt", "altitude") \
.withColumn("data_source", lit('v_data_source')) \
.withColumn("file_date", lit('v_file_date'))\
.withColumn("add_ingestion_date",current_timestamp())

# COMMAND ----------

circuits_renamed_df.describe().show(1)

# COMMAND ----------

circuits_renamed_df.write.mode("overwrite").format("parquet").save('dbfs:/mnt/test3434vgg/processed/circuits/')

# COMMAND ----------

# MAGIC %fs
# MAGIC 
# MAGIC ls /mnt/test3434vgg/processed/circuits/

# COMMAND ----------


