import json

with open("json/sample_data/sample_price.json", mode="r", encoding="utf-8") as read_file:
    reader = json.load(read_file)

    reader["banana"] = {"price": 200}

    with open("json/sample_data/result.json", mode="w", encoding="utf-8") as write_file:
        json.dump(reader, write_file, ensure_ascii=False, indent=2)