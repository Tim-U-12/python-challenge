# python-challenge
The repository contains 4 python scripts. Two of which are simple standalone programmable scripts use to run the other two python scripts containing the functions "analyse_finance"(AF) and "election_analysis"(EA). AF reads over a csv file containing stock information, then prints and exports simple outputs. EA reads over a csv file containing voting information, then applying simple methods to extract information.

analyse_finance() <br>
:input: <br>
  csvpath (str): a string interpretation of the path to a csv file containing information on stocks<br>
  outputpath (str): a string interpretation of the path to where the solution will be exported<br>
:output:<br>
  analysis.csv (csv): csv file containing the following information extracted from the given data;<br>
    - The total number of months included in the dataset<br>
    - The net total amount of "Profit/Losses" over the entire period<br>
    - The changes in "Profit/Losses" over the entire period, and then the average of those changes<br>
    - The greatest increase in profits (date and amount) over the entire period<br>
    - The greatest decrease in profits (date and amount) over the entire period <br>
  terminal output (str): the same information from the analysis.csv<br>
  
election_analysis()<br>
:input:<br>
  csvpath (str): a string interpretation of the path to a csv file containing information on stocks<br>
  outputpath (str): a string interpretation of the path to where the solution will be exported<br>
:output:<br>
  election_analysis.csv (csv): csv file containing the following information extracted from the given data:<br>
    - The total number of votes cast<br>
    - A complete list of candidates who received votes<br>
    - The percentage of votes each candidate won<br>
    - The total number of votes each candidate won<br>
    - The winner of the election based on popular vote<br>
  terminal output (str): the same information from the analysis.csv<br>
    
