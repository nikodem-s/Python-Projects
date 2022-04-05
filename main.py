from requests import get
from pprint import PrettyPrinter
import csv
import getpass
import os

USER_NAME = getpass.getuser()
BASE_URL = "https://api.weatherapi.com/"
JSON_URL = "v1/current.json?key=d903086d988048e8a6c134655220204&q="
# city = input('Enter a city: ')
printer = PrettyPrinter()
city = "Wadowice"

data = get(BASE_URL + JSON_URL + city).json()
location_data = data['location']
weather_data = data['current']
printer.pprint(weather_data.keys())


def print_info():
    print(f"Weather in {city}({location_data['lat']}, {location_data['lon']}) on time {weather_data['last_updated']}: ")
    print(f"Time: {location_data['localtime']}")
    print(f"Temperature: {weather_data['temp_c']}")
    print(f"Feels like tmperature: {weather_data['feelslike_c']}")
    print(f"Wind speed: {weather_data['wind_kph']} km/h")
    print(f"Wind direction: {weather_data['wind_dir']}")
    print(f"Percent of clouds on the sky: {weather_data['cloud']}%")
    print(f"Humidity: : {weather_data['humidity']}%")


def write_csv():
    # fields = ['time', 'temp', 'ftemp', 'wind', 'cloud', 'humidity']
    row = [location_data['localtime'], weather_data['temp_c'], weather_data['feelslike_c'],
           weather_data['wind_kph'], weather_data['cloud'], weather_data['humidity']]
    with open('pogoda.csv', 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(row)
        file.close()


print_info()
write_csv()
