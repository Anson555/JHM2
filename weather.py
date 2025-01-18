import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"]
        
        report = (f"Weather Report for {city}:\n"
                  f"Temperature: {temperature}°C\n"
                  f"Pressure: {pressure} hPa\n"
                  f"Humidity: {humidity}%\n"
                  f"Description: {description.capitalize()}")
        
        return report
    else:
        return "City not found."

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "YOUR_API_KEY"
    print(get_weather(city_name, api_key))
