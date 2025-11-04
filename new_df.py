# Databricks notebook source
data=[(1,"a"),(2,"b"),(3,"c"),(4,"d"),(5,"e"),(6,"f")]
schema=["id","name"]
df=spark.createDataFrame(data=data,schema=schema)

# COMMAND ----------

display(df)

# COMMAND ----------


