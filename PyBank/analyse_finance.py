import csv

'''
TODO:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period
'''

def analyse_finance(csvpath:str):
    num_months = 0

    with open(csvpath, encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csv_reader)

        for row in csv_reader:
            num_months += 1