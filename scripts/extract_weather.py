import requests
import csv
from datetime import datetime

api_key="d785cbca52b02b5f39446459063bde97"
city="coimbatore"

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

responce = requests.get(url)
data = responce.json()

if responce.status_code ==200:
    # for key,value in data.items():
    #     print(f"{key}:{value}")
        weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "description": data["weather"][0]["description"],
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        filename = "../data/weather_raw_data.csv"
        
        with open(filename,mode="a",newline="") as file:
            writer = csv.DictWriter(file , fieldnames=weather.keys())
            
            if file.tell()==0:
                writer.writeheader()
            writer.writerow(weather)
        print("extraction completed")
        
else:
    print("Error fetching data")
