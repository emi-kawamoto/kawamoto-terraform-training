import json

with open("sample_data/sample_score.json", mode="r", encoding="utf-8") as read_file:
    reader = json.load(read_file)

    reader["Hanako"] = {"score": 100, "memo": "花子の成績です"}

    with open("sample_data/result.json", mode="w", encoding="utf-8") as write_file:
        json.dump(reader, write_file, ensure_ascii=False, indent=2)
