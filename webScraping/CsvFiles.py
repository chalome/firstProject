import csv

with open('country_full.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print(row)