"""This is a training program 2."""
import csv

INPUT_FILE_PATH = "sample_data/california_housing_test.csv"
OUTPUT_FILE_PATH = "sample_data/result.csv"

with open(INPUT_FILE_PATH, mode="r", encoding="utf-8") as r:
    reader = csv.reader(r)
    next(reader)

    with open(OUTPUT_FILE_PATH, newline="", mode="w", encoding="utf-8") as w:
        writer = csv.writer(w, delimiter="\t")
        writer.writerow(["緯度", "経度"])
        for row in reader:
            writer.writerow([row[0], row[1]])
