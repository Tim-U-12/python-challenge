import csv

'''
TODO:
DONE - The total number of months included in the dataset
DONE - The net total amount of "Profit/Losses" over the entire period
DONE - The changes in "Profit/Losses" over the entire period, and then the average of those changes
DONE - The greatest increase in profits (date and amount) over the entire period
DONE - The greatest decrease in profits (date and amount) over the entire period
'''

def analyse_finance(csvpath):
    num_months = 0
    net_total = 0
    avg_change = 0
    max_profit_increase = [None, float('-inf')]
    min_profit_decrease = [None, float('inf')]

    with open(csvpath, encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)

        prev_row = None

        # Iterates through the rows in the csv file
        for row in csvreader:
            num_months += 1
            net_total += round(float(row[1]))

            if prev_row == None:
                prev_row = float(row[1])
            else:
                change = float(row[1]) - prev_row
                avg_change += change
                prev_row = float(row[1])

                # Finds the Greatest profit increase & Decrease
                if change > float(max_profit_increase[1]):
                    max_profit_increase = [row[0], round(change)]
                elif change < float(min_profit_decrease[1]):
                    min_profit_decrease = [row[0], round(change)]

        avg_change = round(avg_change / (num_months - 1), 2)

            
