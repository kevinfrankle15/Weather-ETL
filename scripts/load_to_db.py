import pandas as pd
import psycopg2

connection = psycopg2.connect(
    dbname="weatherdb",
    user="postgres",
    password="kevin",
    host="localhost",
    port="5433"
)

df = pd.read_csv("../data/weather_cleaned_data.csv")

cursor = connection.cursor() ## for run SQL

for _,row in df.iterrows():
    cursor.execute("""
                   INSERT INTO weather_data (datetime, city, temperature, humidity, pressure, description) 
                   VALUES (%s,%s,%s,%s,%s,%s)
                   """,(
                       row["datetime"],row["city"],row["temperature"],
                       row["humidity"],row["pressure"],row["description"]
                   ))
connection.commit()
cursor.close()
connection.close()

print("data loaded successfully")