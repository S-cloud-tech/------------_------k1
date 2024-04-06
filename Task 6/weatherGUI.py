import os
import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

load_dotenv()

def get_weather_forecast(api_key, location, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['city']['name']
        forecasts = data['list']
        forecast_text = f"Weather forecast for {city} for the next {days} days:\n\n"
        for forecast in forecasts[:days]:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            humidity = forecast['main']['humidity']
            description = forecast['weather'][0]['description']
            forecast_text += f"Date: {date}\n"
            forecast_text += f"Temperature: {temperature}°C\n"
            forecast_text += f"Humidity: {humidity}%\n"
            forecast_text += f"Conditions: {description}\n\n"
        return forecast_text
    else:
        return messagebox.showinfo(root, message="Failed to fetch weather forecast. Please check your location or API key.", type="yesnocancel")

def fetch_weather_forecast():
    location = location_entry.get()
    days = int(days_entry.get())
    api_key = os.getenv("API_KEY") # Replace with your OpenWeatherMap API key
    forecast_text = get_weather_forecast(api_key, location, days)
    forecast_label.config(text=forecast_text)

# 

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x400")
root.config(bg="#fed7aa")

# Create and place widgets
location_label = tk.Label(root, text="Enter City:", bg="#fb923c", font=("Roboto", 10, 'bold'))
location_label.grid(row=0, column=0, padx=5, pady=5)

location_entry = tk.Entry(root)
location_entry.grid(row=0, column=1, padx=5, pady=5)

days_label = tk.Label(root, text="Number of Days:", bg="#fb923c", font=("Roboto", 10, 'bold'))
days_label.grid(row=1, column=0, padx=5, pady=5)

days_entry = tk.Entry(root)
days_entry.grid(row=1, column=1, padx=5, pady=5)

fetch_button = tk.Button(root, text="Fetch Forecast", bg="#fb923c", command=fetch_weather_forecast)
fetch_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

forecast_label = tk.Label(root, text="", justify="center")
forecast_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


# Run the main event loop
root.mainloop()
