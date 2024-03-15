import json

with open("json/sample_data/sample_price.json", mode="r", encoding="utf-8") as f:
    reader = json.load(f)
    print(json.dumps(reader, indent=2, ensure_ascii=False))