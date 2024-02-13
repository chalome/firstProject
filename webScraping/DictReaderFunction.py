import csv

with open('country_full.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row['name'] + "its alpha-2 " + row['alpha-2'] + "its alpha-5 " + row['alpha-3'] + " country-code " + row['country-code']+" iso_3166-2 "+row['iso_3166-2']+" region "+row['region']+" sub-region "+row['sub-region']+" intermediate-region "+row['intermediate-region']+" region-code "+row['region-code']+" sub-region-code "+row['sub-region-code']+" intermediate-region-code "+row['intermediate-region-code'])