# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.list(scope = 'test928' )

# COMMAND ----------



# COMMAND ----------

storage_account = 'test3434vgg'
client_id = dbutils.secrets.get(scope = 'test928' ,key  ='client-id' )
tenant_id = dbutils.secrets.get(scope = 'test928' ,key  ='tenant-id')
secret_id = dbutils.secrets.get(scope = 'test928' ,key  ='secret-id' )

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": f"{client_id}",
           "fs.azure.account.oauth2.client.secret": f"{secret_id}",
           "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

configs

# COMMAND ----------

dbutils.fs.mount(
  source = f"abfss://raw@{storage_account}.dfs.core.windows.net",
  mount_point = f"/mnt/{storage_account}/raw",
  extra_configs = configs )

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------


dbutils.fs.ls('/mnt/test3434vgg/raw/')

# COMMAND ----------

dbutils.fs.unmount(f"/mnt/{storage_account}/raw")

# COMMAND ----------


