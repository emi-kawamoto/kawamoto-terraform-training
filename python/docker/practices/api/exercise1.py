import requests
import json
import os
from dotenv import load_dotenv

# .env ファイルの内容を読み込む
load_dotenv()

# 環境変数を表示
print(os.environ['API_KEY'])

w_api = os.environ['API_KEY']


url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "Tokyo", "appid": w_api}

res = requests.get(url, params=params)
jsonText = res.json()
print(json.dumps(jsonText, indent=4))