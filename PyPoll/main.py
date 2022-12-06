import os
from election_analysis import election_analysis as ea

if __name__ == "__main__":
    csvpath = os.path.join('.', 'Resources', 'election_data.csv')
    
    ea(csvpath)