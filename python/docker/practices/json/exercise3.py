"""training json program2"""
import json

INPUT_FILE_PATH = "sample_data/sample_price.json"
OUTPUT_FILE_PATH = "sample_data/result.json"

with open(INPUT_FILE_PATH, "r", newline="", encoding="utf-8") as r:
    reader = json.load(r)
    with open(OUTPUT_FILE_PATH, "w+", encoding="utf-8") as w:
        json.dump(reader, w, ensure_ascii=False, indent=2)
