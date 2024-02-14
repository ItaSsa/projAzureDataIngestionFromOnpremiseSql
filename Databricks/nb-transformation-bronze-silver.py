# Databricks notebook source
# MAGIC %md
# MAGIC ## Transforming other tables

# COMMAND ----------

table_name=[]

for tn in dbutils.fs.ls('/mnt/bronze/Person'):
  table_name.append(tn.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp,date_format
from pyspark.sql.types import TimestampType

for tn in table_name:
    path= '/mnt/bronze/Person/'+ tn +'/'+ tn +'.parquet'
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if 'Date' in col or 'date' in col :
            df = df.withColumn(col,
                            date_format(from_utc_timestamp(df[col].cast(TimestampType()),"UTC")
                                        ,'yyyy-MM-dd'))
            
    output_path= '/mnt/silver/Person/'+ tn +'/'
    df.write.format('delta').mode('overwrite').save(output_path)


# COMMAND ----------


