import os
from election_analysis import election_analysis as ea

if __name__ == "__main__":
    csvpath = os.path.join('.', 'Resources', 'election_data.csv')
    outputpath = os.path.join('.', 'analysis', 'election_analysis.csv')
    
    ea(csvpath, outputpath)