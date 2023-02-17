import json

total_score: int = 0
with open("sample_data/sample_score.json", mode="r", encoding="utf-8") as f:
    reader = json.load(f)

    for dic in reader.values():
        total_score += dic["score"]

    print(total_score)
