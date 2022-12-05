import os
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
with open(csvpath, encoding='utf8') as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")

    for row in csv_reader:
        print(row)