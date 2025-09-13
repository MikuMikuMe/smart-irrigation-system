Creating a smart irrigation system with IoT capabilities involves integrating various components such as weather forecasts, soil moisture sensors, and an adaptive scheduling mechanism. Below is a Python program to demonstrate a simplified version of such a system. This example includes basic components, error handling, and comments for clarity.

Please note that in a real-world scenario, additional setup such as connecting to actual hardware devices, setting up web endpoints for weather data, and using a database for storing state information might be needed.

```python
import requests
import random
import time

# Constants for the application
WEATHER_API_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_API_KEY = 'your_openweather_api_key'
LOCATION = 'your_location'  # City name or coordinates
SOIL_MOISTURE_THRESHOLD = 30  # Percentage
CHECK_INTERVAL = 3600  # 1 hour in seconds
ERROR_LOG_FILE = 'error.log'

# Mock function to read soil moisture level
def read_soil_moisture():
    """
    Simulate reading soil moisture from a sensor.
    Replace this with actual hardware interaction code as needed.
    """
    return random.randint(0, 100)  # Random value simulating sensor output

def get_weather_forecast():
    """
    Fetch the current weather for the specified location using OpenWeatherMap API.
    """
    try:
        response = requests.get(
            WEATHER_API_URL,
            params={'q': LOCATION, 'appid': WEATHER_API_KEY, 'units': 'metric'}
        )
        response.raise_for_status()
        data = response.json()
        return data['weather'][0]['main'], data['main']['temp']
    except requests.RequestException as e:
        log_error(f'Weather API request failed: {e}')
        return None, None

def should_irrigate(soil_moisture, weather_condition, temperature):
    """
    Determine whether irrigation is necessary based on soil moisture, weather, and other parameters.
    """
    if soil_moisture < SOIL_MOISTURE_THRESHOLD:
        if weather_condition.lower() in ['rain', 'drizzle']:
            return False
        return True
    return False

def activate_irrigation():
    """
    Simulate activation of irrigation system.
    Replace this with actual hardware interaction code as needed.
    """
    print("Irrigation system activated.")

def log_error(message):
    """
    Log an error message to a file.
    """
    with open(ERROR_LOG_FILE, 'a') as file:
        file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - {message}\n')

def main():
    """
    Main function for running the smart irrigation system.
    """
    while True:
        try:
            soil_moisture = read_soil_moisture()
            weather_condition, temperature = get_weather_forecast()

            if weather_condition is None:  # Error occurred during weather fetching
                print("Skipping this cycle due to weather data retrieval failure.")
                time.sleep(CHECK_INTERVAL)
                continue

            print(f"Soil moisture: {soil_moisture}% | Weather: {weather_condition} | Temp: {temperature}°C")

            if should_irrigate(soil_moisture, weather_condition, temperature):
                activate_irrigation()
            else:
                print("Irrigation not required.")

            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            log_error(f'Unexpected error: {e}')
            print("An unexpected error occurred, check the error log for details.")
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
```

### Important Notes:

1. **Weather API**: Replace `'your_openweather_api_key'` and `'your_location'` with your OpenWeatherMap API key and desired location, respectively.
2. **Error Handling**: The program handles possible HTTP request exceptions and logs them to a file named `error.log`.
3. **Simulated Sensors**: The program includes a simulated soil moisture sensor value. Replace it with real sensor data if using actual hardware.
4. **Irrigation Simulation**: The function `activate_irrigation` should interact with an actual relay or other hardware component in a practical application.
5. **Execution Interval**: The loop runs at an interval set by `CHECK_INTERVAL`, which is set to 1 hour in this example. Adjust as needed for your use case.

This program serves as a basic prototype of the smart irrigation system and can be extended to fit specific needs and incorporate actual IoT devices.