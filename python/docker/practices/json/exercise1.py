"""training json program1"""
import json

FILE_PATH = "sample_data/sample_price.json"

with open(FILE_PATH, "r", encoding="utf-8") as f:
    reader = json.load(f)
    print(json.dumps(reader, indent=2, ensure_ascii=False))
