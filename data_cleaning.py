

import pandas as pd
import logging 
import time

logging.basicConfig(
    filename= "logs/etl.logs",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s"

)
logging.info("ETL PIPELINE STARTED")

df = pd.read_csv("messy_customer_sales_data.csv")

start_time = time.time()
logging.info("START TIME")

print(df.isnull().sum())

df = df.fillna(0)

print(df.isnull().sum())

df = df.dropna(subset= "Customer_ID")
df.drop_duplicates(subset= "Customer_ID", inplace= True)
print(df.duplicated(subset= "Customer_ID"))

df["Name"] = df["Name"].str.capitalize()
df["Gender"] = df["Gender"].str.capitalize().str.strip()

df["Gender"] = df["Gender"].replace({"m" : "Male" , "f" : "Female", "M" : "Male", "F" : "Female"})

logging.info("CLEAN DATA")

print(df["Gender"])
print(df["Name"])
print(df["Customer_ID"].value_counts())

logging.info("ETL PIPLINE SUCCESSFULL")