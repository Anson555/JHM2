pip install requests
import requests

# Replace 'your_api_key' with your actual API key
api_key = "your_api_key"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get city name from user input
city_name = input("Enter city name: ")
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# Make the request and get the response
response = requests.get(complete_url)
data = response.json()

# Check if the city is found
if data["cod"] != "404":
    main = data["main"]
    weather = data["weather"][0]
    temperature = main["temp"]
    pressure = main["pressure"]
    humidity = main["humidity"]
    description = weather["description"]

    print(f"Temperature: {temperature}K")
    print(f"Atmospheric pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    print(f"Weather description: {description}")
else:
    print("City not found.")
