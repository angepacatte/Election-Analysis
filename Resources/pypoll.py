
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election-Analysis","Resources", "election_results.csv")
#Assign a variable to save th file to a path
file_to_save = os.path.join("Election-Analysis","analysis", "election_analysis.txt")
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read th file object with reader function.
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)