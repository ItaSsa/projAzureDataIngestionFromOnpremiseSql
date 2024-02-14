# Databricks notebook source
# MAGIC %md
# MAGIC ## Import functions

# COMMAND ----------

# MAGIC %run /Shared/nb-utils-functions

# COMMAND ----------

# MAGIC %md
# MAGIC ## Mount Storage Account Containers

# COMMAND ----------

# Containers to mount
containers_list = ['bronze','silver','gold']
storage_account_name='adlitainplaceprojects'

# COMMAND ----------

#mounting containers to abfs
for container_name in containers_list:
    mount_name = container_name
    mountStorageAccountCredentialPassthrough(storage_account_name,container_name,mount_name)

# COMMAND ----------

#Testing...
display(dbutils.fs.ls('/mnt/bronze'))

# COMMAND ----------


