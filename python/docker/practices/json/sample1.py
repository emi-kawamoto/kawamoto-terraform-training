import json

with open(
    "/root/practices/json/sample_data/sample_score.json", mode="r", encoding="utf-8"
) as f:
    reader = json.load(f)
    print(json.dumps(reader, indent=2, ensure_ascii=False))
