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

import datetime as dt

# use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()

#print the present time
print("The time right now is ", now)

dir(dt)

#add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #write three counties to the file 
    txt_file.write('Counties in the election\n------------------\nAraphoe\nDenver\nJefferson')



