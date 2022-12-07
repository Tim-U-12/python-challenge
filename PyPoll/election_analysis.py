import csv

def election_analysis(csvpath:str, outputpath:str):
    poll = {}

    # Read through the csv file and add the candidate and their number of votes into a dictionary
    with open(csvpath, 'r',encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)

        for row in csvreader:
            if row[2] in poll:
                poll[row[2]] += 1
            else:
                poll[row[2]] = 1

    # Sum the number of votes each candidate got | found the highest number of votes
    total_votes = sum(poll.values())
    winner = max(poll, key=poll.get)

    # Export results to csv file
    with open(outputpath, 'w', encoding='utf8', newline='') as outputfile:
        outputwriter = csv.writer(outputfile, delimiter=' ')

        
        outputwriter.writerow("Election Results".split(' '))
        outputwriter.writerow(["-------------------------"])

        outputwriter.writerow(f"Total Votes: {total_votes}".split(' '))
        outputwriter.writerow(["-------------------------"])

        for candidate in poll:
            outputwriter.writerow(f"{candidate}: {round((poll[candidate]/total_votes) * 100, 3)}% ({poll[candidate]})".split(' '))
        outputwriter.writerow(["-------------------------"])

        outputwriter.writerow(f"Winner: {winner}".split(' '))
        outputwriter.writerow(["-------------------------"])
    
    # Print the output
    with open(outputpath, 'r', encoding='utf8') as printfile:
        printreader = csv.reader(printfile, delimiter='\n')

        for row in printreader:
            print(row[0])