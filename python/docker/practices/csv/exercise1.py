import csv

with open("sample_data/california_housing_test.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)

        