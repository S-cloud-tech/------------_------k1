import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
    else:
        print("Failed to fetch weather data. Please check your location or API key.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_app.py <city>")
        sys.exit(1)
    
    api_key = os.getenv("API_KEY")
    location = ' '.join(sys.argv[1:])
    get_weather(api_key, location)
