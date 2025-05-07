import os
import requests

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "kr"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    description = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    return f"{city}의 현재 날씨는 {description}, 기온은 {temp}°C입니다."
