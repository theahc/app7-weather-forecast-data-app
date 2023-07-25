import os
import requests

API_KEY = os.getenv("OPENWEATHER")

def get_data(place, forecast_days=None):
    if not API_KEY:
        raise ValueError("OpenWeatherMap API key is missing. Set the OPENWEATHER environment variable.")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=1))
