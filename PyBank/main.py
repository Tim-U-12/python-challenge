from analyse_finance import analyse_finance as af
import os

if __name__ == "__main__":
    csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
    af(csvpath)