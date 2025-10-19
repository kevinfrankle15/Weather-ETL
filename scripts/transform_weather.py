import pandas as pd
from datetime import datetime

raw_csv = "../data/weather_raw_data.csv"
cleaned_csv = "../data/weather_cleaned_data.csv"

try:
    
    df = pd.read_csv(raw_csv)

    df.drop_duplicates(inplace=True)

    df["datetime"] = pd.to_datetime(df["datetime"],errors="coerce")

    df.fillna({
        "temperature":df["temperature"].mean(),
        "humidity":df["humidity"].mean(),
        "pressure":df["pressure"].mean(),
        "description":"unknown"
    },inplace=True)

    df=df[["datetime", "city", "temperature", "humidity", "pressure", "description"]]

    df.sort_values(by="datetime",inplace=True)

    df.to_csv(cleaned_csv,index=False)
except FileNotFoundError:
    print("file not found , run extract file")
except Exception as e:
    print("error during transformation")

