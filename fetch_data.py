import csv
import requests
import json

API_KEY = ""

coords = []
data = {}

with open('gps.csv', encoding='utf-8-sig') as csv_file:
    file = csv.reader(csv_file, delimiter=';')
    for row in file:
        coords.append(row)

for c in coords:
    lat = c[0]
    lon = c[1]

    data[f"{lat},{lon}"] = {}

    url = f"http://pro.openweathermap.org/data/2.5/air_pollution" \
          f"/history?lat={lat}&lon={lon}" \
          f"&start=1606266000&end=1662751240" \
          f"&APPID={API_KEY}"

    air_request = requests.get(url)
    air_data = air_request.json()
    data[f"{lat},{lon}"]["pollution"] = air_data["list"]

    url = f"http://history.openweathermap.org/data/2.5/history" \
          f"/city?lat={lat}&lon={lon}&type=hour" \
          f"&start=1606266000&end=1662751240" \
          f"&appid={API_KEY}"

    weather_request = requests.get(url)
    weather_data = weather_request.json()
    data[f"{lat},{lon}"]["weather"] = weather_data["list"]
    print(len(data))

with open('data.json', 'w+') as f:
    json.dump(data, f, indent=4)
