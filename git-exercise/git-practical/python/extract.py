import os
import urllib.request as req

url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
filename = 'tenki.json'
dir = 'json'
req.urlretrieve(url, os.path.join(dir, filename))