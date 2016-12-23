import csv

with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title 1", "Title 2", "Title 3"])
    writer.writerow(["Data 1", "Data 2", "Data 3"])
    writer.writerow(["Data 4", "Data 5", "Data 6"])

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Data 7", "Data 8", "Data 9"])

with open("data.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

with open("data.csv", "a") as csvfile:
    fieldnames = ["Title 1", "Title 2", "Title 3"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"Title 1": "Write", "Title 2": "with", "Title 3": "Dictionary"})
