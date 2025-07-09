import requests  # Used to make API call (for weather data)
import os    # Used to access environment variables (for API key)
from dotenv import load_dotenv  # Used to load environment variables from .env file

def get_weather(city_name, api_key):

 # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters to send with the request
    params = {
        'q': city_name,       #  City name provided by user
        'appid': api_key,     #  Your API key
        'units': 'metric'     #  Celsius temperature
    }

    # Send GET request to the weather API
    response = requests.get(base_url, params=params)
    

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Convert response to Python dictionary

        # Extract useful data from response
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']

        # Display the results
        print(f"\n Weather in {city_name.capitalize()}:")
        print(f" Temperature: {temperature}°C")
        print(f" Humidity: {humidity}%")
        print(f" Condition: {condition.capitalize()}")

    else:
        print(" Error: City not found or something went wrong.")
        print(" Tip: Small villages might not be available in weather data.")
        print(" Try entering a nearby city or district (e.g., Narowal, Shakargarh).")
   
def main():
    print("☁️ Welcome to the Weather App ☁️")

    #  Step 1: User-specified city input

    city = input("Enter the name of the city you want weather for: ")

    #  Step 2: Your personal OpenWeatherMap API key
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("API_KEY")  # Replace this with your real API key
   
    #  Step 3: Get weather
    get_weather(city, api_key)

#  Entry point of the program
if __name__ == "__main__":
    main()
