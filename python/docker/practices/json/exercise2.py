import json

total_price: int = 0
with open("json/sample_data/sample_price.json", mode="r", encoding="utf-8") as f:
    reader = json.load(f)

    for dic in reader.values():
        total_price += dic["price"]

    print(total_price)