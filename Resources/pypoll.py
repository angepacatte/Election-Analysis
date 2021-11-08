
import csv
import os
#Assign a variable for the file to load and the path.
<<<<<<< Updated upstream
file_to_load = os.path.join("Election-Analysis","Resources", "election_results.csv")
#Assign a variable to save th file to a path
file_to_save = os.path.join("Election-Analysis","analysis", "election_analysis.txt")
=======
file_to_load = os.path.join('/Users/angelapacatte/Documents/Homework/Election-Analysis/Resources/election_results.csv')
#Assign a variable to save th file to a path
file_to_save = os.path.join('..', 'Analysis', 'Analysis.txt')
# 1. Iniialize a total vote counter
total_votes = 0

#Candidate Options
candidate_options = []

#1. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

>>>>>>> Stashed changes
#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read th file object with reader function.
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file.
    headers = next(file_reader)
<<<<<<< Updated upstream
    print(headers)
=======
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1

#Print the candidate name for each row.
        candidate_name = row[2]

#If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:
            #Add it to the list of the candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

            #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save the results to our text file.

# Save the final vote count to the text file.
    #txt_file.write(election_results)
          
            
    #Iterate through the candidate list.
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #Print out each candidate's name, vote count, and percentage of
    #votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percent =
        # vote precentage
        winning_count = votes
        winning_percentage = vote_percentage    
    #Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
#To do: print out winning candidate, vote count and percentage to terminal

winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"--------------------------\n")

#Print the candidate name and percentage of votes.
#print(winning_candidate_summary)


       
>>>>>>> Stashed changes
