#Pseudocode for election data

# # Write down list of candidates
# assign the candidates variable names
#Loop through candidates
    # get their id numbers
    #get counties who voted for them
#calculate total vote of each candidate
#loop through all voters
#for each voter id, determine who they voted for
#output each candidate's vote total
#add them all up to get total votes cast

#add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1.initialize a total vote counter
total_votes = 0

#list of candidates
candidate_options = []
#dictionary of each candidate's vote totals - declaring empty dictionary
candidate_votes = {}

#Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
 
    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        # 2. add to total vote count
        total_votes += 1
        
        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate doesn't match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote total
            candidate_votes[candidate_name] = 0

        #each candidate gets a vote when voted for
        candidate_votes[candidate_name] += 1

# 3. print the candidate vote dictionary
#print(candidate_votes)

#calculate each candidate's vote percentage
# 1. iterate through candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    # 3. calculate percentage of each candidate
    vote_percentage = float(votes) / int(total_votes) * 100

    #print out each candidate's name, vote count, and percentage of
    #their votes to the terminal
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")


    #determine winning vote count and candidate
    # 1. determine if votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. if true, set winning count = votes and winning percentage = 
        #vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning candidate to the candidate's name
        winning_candidate = candidate_name

        winning_candidate_summary = (f"------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote Count: {winning_count:,}\n"
        f"Winning Percentge: {winning_percentage: .1f}%\n"
        f"---------------\n")

print(winning_candidate_summary)
        

