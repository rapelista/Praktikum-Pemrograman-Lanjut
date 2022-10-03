import csv

with open("file.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["Budi Budiman", "17/11/2000"])
    writer.writerow(["Yudi Budiman", "17/11/2001"])

with open("file.csv", "r") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        print(row)
