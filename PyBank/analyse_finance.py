import csv

def analyse_finance(csvpath):
    num_months = 0
    net_total = 0
    avg_change = 0

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

        avg_change = round(avg_change / (num_months - 1), 2)

            
