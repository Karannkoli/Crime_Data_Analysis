import pymysql
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

conn=pymysql.connect(host="127.0.0.1",
               user="root",
               password="Vedant@2001",
               database="crime_database")

query="select * from crime_database"
df=pd.read_sql(query,conn)



conn.close()
print(df)
