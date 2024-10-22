# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# # Initialize variables to track the election data
# total_votes = 0 # why 0? starting off  total count at 0?

# # Define lists and dictionaries to track candidate names and vote counts
# can_name = [] #**** will the names be repated? how to make unique 
# candidate = []

# Winning Candidate and Winning Count Tracker
total_votes = 0
can_count = {}
candidate =[ ] 

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1  #tracker adding all vote count in each of the rows * adds each vote after starting off at 0 

        # Get the candidate's name from the row
        candidate = row[2] #placement of the candidate name in data form 0-2

        # If the candidate is not already in the candidate list, add them
        if candidate in can_count:
         can_count[candidate] +=1

        # Add a vote to the candidate's count
        else:
         can_count[candidate] = 1 #starts new candidate count back to 1 

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print (f'Total Votes :{ total_votes}') # ** Will this go to the terminal Yes right like the summary??

    # Write the total vote count to the text file
    txt_file.write(f'Total Votes :{ total_votes}') # .written is the function to add writing to the file text_file


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidates, count in can_count.items():
        # Get the vote count and calculate the percentage
        percent_vote = (count / total_votes) * 100

        # Update the winning candidate if this one has more votes
        winning_candidate = " " # will be filled in with name of winner candidate 
        winning_count = 0 #start off count at 0

        if count > winning_count: # with an if statment to count if 
           winning_count = count 
           winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        print (f'{candidate}: {percent_vote}')

#     # Generate and print the winning candidate summary
#  candidate_summary = (

#      "Election Results \n"
#      "--------------- \n"
#      f'Total Votes :{total_votes}\n'
#      "-------------- /n"
#      f'Charles Casper Stockham:{ }\n'
#      f'Diana DeGettte:{ }\n'
#      f'Raymon Anthony Doane:{ } \n'
#      "------------\n"
#      f'Winner:{ }\n'
#      "------------- \n'
#      )

#     # Save the winning candidate summary to the text file
# print(candidate_summary)
