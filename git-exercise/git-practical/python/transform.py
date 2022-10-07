import json
import pandas as pd

with open('json/tenki.json', 'r', encoding="UTF-8") as f:
  data = json.load(f)

dataLists1 = []
columns1 = ['report_datetime', 'name', 'time_define', 'weather_code']

for area in data:
  name = area['name']
  reportDatetime = area['srf']['reportDatetime']
  for ts in area['week']['timeSeries']:
    times = [n for n in ts['timeDefines']]
    if 'weatherCodes' in ts['areas']:
      for i,v in enumerate(ts['areas']['weatherCodes']):
        tmpDataList = []
        tmpDataList.append(reportDatetime)
        tmpDataList.append(name)
        tmpDataList.append(times[i])
        tmpDataList.append(v)
        dataLists1.append(tmpDataList)

df1 = pd.DataFrame(data=dataLists1, columns=columns1)
df1['report_datetime'] = df1['report_datetime'].astype(str)
df1['name'] = df1['name'].astype(str)
df1['time_define'] = df1['time_define'].astype(str)
df1['weather_code'] = df1['weather_code'].astype(int)

with open('json/weatherCodes.json', 'r', encoding="UTF-8") as f:
  data2 = json.load(f)

dataLists2 = []
columns2 = ['weather_code', 'fig_day', 'fig_night', 'roughly_code', 'exp_jp', 'exp_en']

for code in data2:
  tmpDataList2 = [code]
  dataLists2.append(tmpDataList2 + data2[code])

df2 = pd.DataFrame(data=dataLists2, columns=columns2)
df2['weather_code'] = df2['weather_code'].astype(int)
df2['fig_day'] = df2['fig_day'].astype(str)
df2['fig_night'] = df2['fig_night'].astype(str)
df2['roughly_code'] = df2['roughly_code'].astype(int)
df2['exp_jp'] = df2['exp_jp'].astype(str)
df2['exp_en'] = df2['exp_en'].astype(str)

result = pd.merge(df1, df2, how= 'left', on = 'weather_code')

result.to_csv('dim_cities.csv', index = False)