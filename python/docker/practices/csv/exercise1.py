"""This is a training program 1."""
import csv

FILE_PATH = "sample_data/california_housing_test.csv"
with open(FILE_PATH, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)
