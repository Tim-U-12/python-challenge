import csv

'''
CSV breakdown:
- Voter ID
- County
- Candidate
'''

def election_analysis(csvpath:str):
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

    total_votes = sum(poll.values())
    winner = max(poll, key=poll.get)

    print(poll)
    print(winner)
      
        



        
        