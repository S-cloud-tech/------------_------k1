import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# def get_weather(api_key, location):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         city = data['name']
#         temperature = data['main']['temp']
#         humidity = data['main']['humidity']
#         description = data['weather'][0]['description']
#         print(f"Weather in {city}:")
#         print(f"Temperature: {temperature}°C")
#         print(f"Humidity: {humidity}%")
#         print(f"Conditions: {description}")
#     else:
#         print("Failed to fetch weather data. Please check your location or API key.")

# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Usage: python weather_app.py <city>")
#         sys.exit(1)
    
#     api_key = os.getenv("API_KEY")
#     location = ' '.join(sys.argv[1:])
#     get_weather(api_key, location)

def get_weather(api_key, location, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['city']['name']
        forecasts = data['list']
        print(f"Weather forecast for {city} for the next {days} days:")
        for forecast in forecasts[:days]:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            humidity = forecast['main']['humidity']
            description = forecast['weather'][0]['description']
            print(f"Date: {date}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {description}\n")
    else:
        print("Failed to fetch weather forecast. Please check your location or API key.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python weather_forecast.py <city> <days>")
        sys.exit(1)
    
    api_key = os.getenv("API_KEY")
    location = sys.argv[1]
    days = int(sys.argv[2])
    get_weather(api_key, location, days)
