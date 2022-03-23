# Databricks notebook source

msg = 'hello'

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select 'hello'

# COMMAND ----------

# MAGIC %scala
# MAGIC 
# MAGIC var msg = "hello"

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Notebook Intro

# COMMAND ----------

# MAGIC %fs

# COMMAND ----------

# MAGIC %sh
# MAGIC ps

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

for folder_name in dbutils.fs.ls('/'):
    print(folder_name)

# COMMAND ----------

dbutils.notebook.run('/Users/a10584931@gmail.com/01_practice',10 )

# COMMAND ----------

#dbutils.widgets.input()

# COMMAND ----------


