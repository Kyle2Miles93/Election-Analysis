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
    
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #print the final vote total to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # 3. calculate percentage of each candidate
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        
        # print each candidate, their voter total, and percentage to the terminal
        print(candidate_results)
        # save the candidate results to our text file.
        txt_file.write(candidate_results)

        # determine winning vote count and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # print the winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote Count: {winning_count:,}\n"
        f"Winning Percentge: {winning_percentage: .1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
            

