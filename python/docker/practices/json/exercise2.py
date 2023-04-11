"""training json program2"""
import json

FILE_PATH = "sample_data/sample_price.json"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    reader = json.load(f)
    dic = reader.values()

    print(sum(map(lambda x: x['price'], dic)))
