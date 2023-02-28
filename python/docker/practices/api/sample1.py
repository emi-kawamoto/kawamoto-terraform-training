import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "Tokyo", "appid": "xxx(作成したAPIKEYを記載してください)"}

res = requests.get(url, params=params)
jsonText = res.json()
print(json.dumps(jsonText, indent=4))
