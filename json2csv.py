import csv
import json

header = [
    "ID",
    "Latitude",
    "Longitude",
    "Date",
    "PM2.5",
    "PM10",
    "Pollution dataset count",
    "Temperature",
    "Humidity",
    "Wind speed",
    "Weather dataset count"
]

with open('new_data.json') as f:
    data = json.load(f)
    print('DATA LOADED SUCCESSFULLY')

    rows = []

    for item in data:
        for idx, _ in enumerate(item):
            for i, key in enumerate(data[idx].keys()):
                if i >= 2:
                    if list(data[idx][key].values())[-1] != 0 or list(data[idx][key].values())[-2] != 0:
                        row = []
                        row.append(int(len(rows)) + 1)
                        row.append(list(data[idx].values())[0])
                        row.append(list(data[idx].values())[1])
                        row.append(key)
                        for k, v in data[idx][key].items():
                            row.append(v)
                        print(row)
                        rows.append(row)

with open('data.csv', 'w+', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for row in rows:
        writer.writerow(row)
