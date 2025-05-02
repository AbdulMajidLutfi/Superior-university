import csv
import requests
class Weather:
    def __init__(self, temperature, humidity, pressure, wind_speed):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self._wind_speed = wind_speed

    def save_to_csv(self, location):
        with open('weather_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([location,
                             self._temperature,
                             self._humidity,
                             self._pressure,
                             self._wind_speed])
class WeatherAPI:
    def __init__(self, api_key):
        self._api_key = api_key
    def fetch_weather(self, location):
        raise NotImplementedError()
class CurrentWeather(Weather):
    pass
class OpenWeatherAPI(WeatherAPI):
    def fetch_weather(self, location):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self._api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200 or 'main' not in data or 'wind' not in data:
            return None, data.get('message', 'Unknown error')
        weather = CurrentWeather(
            data["main"]["temp"],
            data["main"]["humidity"],
            data["main"]["pressure"],
            data["wind"]["speed"])
        return weather, None
