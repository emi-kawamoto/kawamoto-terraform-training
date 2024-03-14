import csv

with open(
    "sample_data/california_housing_test.csv", mode="r", encoding="utf-8"
) as read_file:
    reader = csv.reader(read_file)
    next(reader)

    with open(
        "sample_data/result.csv", newline="", mode="w", encoding="utf-8"
    ) as write_file:
        writer = csv.writer(write_file, delimiter="\t")
        writer.writerow(["緯度", "軽度"])
        for row in reader:
            writer.writerow([row[2], row[3]])