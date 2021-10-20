import datetime
import json
import time

with open('data.json') as f:
    data = json.load(f)
    print('DATA LOADED SUCCESSFULLY')

all_dates = []

for item in data:
    for idx, pollution in enumerate(data[item]['pollution']):
        dt = data[item]['pollution'][idx]['dt']
        date = datetime.datetime.fromtimestamp(dt).strftime('%d.%m.%Y')
        data[item]['pollution'][idx]['dt'] = date
        all_dates.append(date)

    for idx, weather in enumerate(data[item]['weather']):
        dt = data[item]['weather'][idx]['dt']
        date = datetime.datetime.fromtimestamp(dt).strftime('%d.%m.%Y')
        data[item]['weather'][idx]['dt'] = date
        all_dates.append(date)

unique_dates = list(set(all_dates))

new_data = []

for idx, item in enumerate(data):
    lat, lon = item.split(',')

    dic = {'lat': lat, 'lon': lon}

    for date in unique_dates:
        dic[date] = {}
        dic[date]['pm2_5'] = 0
        dic[date]['pm10'] = 0
        dic[date]['pollution_count'] = 0
        dic[date]['temp'] = 0
        dic[date]['humidity'] = 0
        dic[date]['wind_speed'] = 0
        dic[date]['weather_count'] = 0

    print(f'ITEM NUMBER {idx}')

    for idx, pollution in enumerate(data[item]['pollution']):
        dic[date]['pm2_5'] = (dic[date]['pm2_5'] * dic[date]['pollution_count'] + data[item]['pollution'][
            idx]['components']['pm2_5']) / (dic[date]['pollution_count'] + 1)
        dic[date]['pm10'] = (dic[date]['pm10'] * dic[date]['pollution_count'] + data[item]['pollution'][
            idx]['components']['pm10']) / (dic[date]['pollution_count'] + 1)
        dic[date]['pollution_count'] += 1

    for idx, weather in enumerate(data[item]['weather']):
        dic[date]['temp'] = (dic[date]['temp'] * dic[date]['weather_count'] + data[item]['weather'][idx][
            'main']['temp']) / (dic[date]['weather_count'] + 1)
        dic[date]['humidity'] = (dic[date]['humidity'] * dic[date]['weather_count'] +
                                 data[item]['weather'][idx][
                                     'main']['humidity']) / (dic[date]['weather_count'] + 1)
        dic[date]['wind_speed'] = (dic[date]['wind_speed'] * dic[date]['weather_count'] +
                                   data[item]['weather'][idx][
                                       'wind']['speed']) / (dic[date]['weather_count'] + 1)
        dic[date]['weather_count'] += 1

    print(dic)
    new_data.append(dic)

print('DATA MANIPULATED SUCCESSFULLY')
print('DATA LENGTH: ' + str(len(new_data)))

with open('new_data.json', 'w+') as f:
    json.dump(new_data, f, indent=4)

print('DATA DUMPED SUCCESSFULLY')
