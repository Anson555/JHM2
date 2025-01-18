pip install requests
import requests
import json

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'your_api_key'
CITY = 'Kowloon City'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def get_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']
        
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']} hPa")
        print(f"Weather Description: {weather_description}")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    weather_data = get_weather_data(URL)
    display_weather(weather_data)
