import csv

with open("tes.csv", mode="w", newline="") as file:
    fieldnames = ["nama", "tgl"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"nama": "Budi Budiman", "tgl": "17/11/2000"})
    writer.writerow({"nama": "Yudi Budiman", "tgl": "17/12/2001"})

with open("tes.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        print(row)
