# Databricks notebook source
# DBTITLE 1,Install kaggle for this session
# MAGIC %pip install kaggle

# COMMAND ----------

import os
os.environ["KAGGLE_USERNAME"]="bilbro"
os.environ["KAGGLE_KEY"]="2323af66bafa054e98e006c386f00c4b"

# COMMAND ----------

# DBTITLE 1,Download E-Commerce data from kaggle
# MAGIC %sh
# MAGIC kaggle datasets download -d mlg-ulb/creditcardfraud

# COMMAND ----------

# MAGIC %sh
# MAGIC unzip creditcardfraud.zip

# COMMAND ----------

# DBTITLE 1,Move data into Azure cloud-object storage (ADLS gen2)
dbutils.fs.mv("file:/Workspace/Repos/lucas.bilbro@databricks.com/CCFraud/creditcard.csv", "dbfs:/Bilbro/files/FraudDemo/creditcard.csv")

# COMMAND ----------

# DBTITLE 1,Create a database and table using the raw data
# MAGIC %sql 
# MAGIC create database if not exists usps_demo;
# MAGIC use usps_demo;
# MAGIC drop table if exists CCFraud_raw;
# MAGIC 
# MAGIC create table CCFraud_raw 
# MAGIC using csv 
# MAGIC options (header "true") 
# MAGIC Location 'dbfs:/Bilbro/files/FraudDemo/creditcard.csv';

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from usps_demo.CCFraud_raw

# COMMAND ----------


