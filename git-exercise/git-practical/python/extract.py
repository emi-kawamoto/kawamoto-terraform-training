import os
import urllib.request as req

url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
dir = 'json'
data = req.urlopen(url).read()
with open(os.path.join(dir, filename), mode="wb") as f:
    f.write(data)