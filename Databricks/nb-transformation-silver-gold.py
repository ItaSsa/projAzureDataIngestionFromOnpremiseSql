# Databricks notebook source
# Checking content
display(dbutils.fs.ls('/mnt/silver/Person'))

# COMMAND ----------

table_name = []
for tn in dbutils.fs.ls('/mnt/silver/Person'):
    table_name.append(tn.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    path='/mnt/silver/Person/'+name
    print(path)
    df = spark.read.format('delta').load(path)

    #Getting column list
    column_names = df.columns

    for old_column_name in column_names:
        # Convert  from ColumnName to Column_Name format
        new_column_name =  "".join(['_' + char if char.isupper() and not old_column_name[i-1].isupper() 
                                    else char for i,char in enumerate(old_column_name)]).lstrip("_")
     

        df = df.withColumnRenamed(old_column_name,new_column_name)

    output_path='/mnt/gold/Person/'+name+'/'
    df.write.format('delta').mode('overwrite').save(output_path)
    


# COMMAND ----------

display(dbutils.fs.ls("/mnt/gold/Person"))

# COMMAND ----------


