import os
import requests
from dotenv import load_dotenv

load_dotenv('weather.env')
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city_name,
        "appid": API_KEY,      
        "units": "metric",
        "lang": "ru"   
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
        
    print(f" Погода в городе {data['name']}:")
    print(f"   Температура: {temp}°C")
    print(f"   Описание: {description.capitalize()}")

city = input("Введите название города: ")
get_weather(city)