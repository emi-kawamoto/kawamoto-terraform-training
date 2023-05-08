import csv

with open(
    "/root/practices/csv/sample_data/california_housing_train.csv",
    mode="r",
    encoding="utf-8",
) as read_file:
    reader = csv.reader(read_file)
    next(reader)

    with open(
        "/root/practices/csv/sample_data/result.csv",
        newline="",
        mode="w",
        encoding="utf-8",
    ) as write_file:
        writer = csv.writer(write_file, delimiter="\t")
        writer.writerow(["築年数", "部屋数"])
        for row in reader:
            writer.writerow([row[2], row[3]])
