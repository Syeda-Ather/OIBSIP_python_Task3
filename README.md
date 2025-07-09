# OIBSIP - Python Programming Task 3: Weather App

##  Task Title:
Basic Weather App

##  Objective:
To build a Python-based weather application that allows the user to fetch real-time weather data for any city using the OpenWeatherMap API and display temperature, humidity, and conditions.

##  Tools & Technologies:
-   VS Code
- **Language:** Python 3.x
- **Libraries Used:**
- **API Used:** OpenWeatherMap API
  - `requests` – For making API calls
  - `os` – To access environment variables
  - `dotenv` – To securely load environment variables from `.env` file


##  Features:
- Simple terminal-based interface
- User inputs any city name
- Fetches:
  -  Temperature (in Celsius)
  -  Humidity (in %)
  -  Weather condition (e.g., Clear, Rain, Clouds)
- Gracefully handles errors like:
  - Invalid or misspelled cities
  - Cities not available in weather database
- Secure API key usage via `.env` file

##  Files Included:
- `weather_app.py` — Main Python script
- `.env` — Stores the API key (not uploaded to GitHub)
- `.gitignore` — Prevents `.env` file from being pushed to GitHub
- `README.md` — This documentation file
- `screenshots/` — folder containing screenshots of the code

---

##  API Key Security:

This project uses a `.env` file to safely store the API key.

 Make sure to:
- Replace with your actual API key
- Keep `.env` file **private**
- Add `.env` to `.gitignore` so it doesn’t get uploaded

---

##  How It Works:

1. User runs the script from terminal
2. Script asks for the city name
3. OpenWeatherMap API is called with the provided city
4. Real-time weather data is fetched
5. Output is displayed:
   - Temperature (°C)
   - Humidity (%)
   - Weather condition (e.g., cloudy, clear, etc.)
6. Error message appears if city not found
---

##  Sample Output:
☁️ Welcome to the Weather App ☁️
Enter the name of the city you want weather for: Lahore

Weather in Lahore:
Temperature: 34°C
Humidity: 60%
Condition: Clear sky
---

##  Screenshots:
Screenshots of the code are provided inside the `screenshots_weather_app/` folder.
---

##  Author:
Syeda Ather Fatima
---

>  This task is submitted as part of the **OIBSIP Internship Program (Python Programming Domain)**.
