# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies 
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 #start off count at 0
total_net = 0  #start off count at 0
great_increase = -float('inf')
great_decrease = float('inf')
previous_change = 0 #start off count at 0
monthly_changes = [ ]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
   
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1 # counts the month after row header


        #track profit/loss
        total_net += int(row[1])
       

        # Track the net change
        monthly_change = int(row[1]) - previous_change 
        previous_change = int(row[1])
        monthly_changes.append(monthly_change)


 # Calculate the greatest increase in profits (month and amount)
        if monthly_change > great_increase:
            great_increase = monthly_change
            month_increase = row[0]
        # Calculate the greatest decrease in losses (month and amount)
        elif monthly_change > great_decrease:
            month_decrease = row[0]
            great_decrease = monthly_change
            
        average = (sum(monthly_changes)-monthly_changes[0] / 85)
        
# Calculate the average net change across the months
         

 #average formula using the amount of list and the summ of all list 

out_summary = (
    "Financial Analysis\n"
    "----------------------------\n"
    f'Total_months: {total_months}\n'
    f'Total net: $ {total_net}\n'
    f'Average Change: ${average}\n'
    f"Greastest Increase in Profits: {great_increase}\n"
    f"Greastest Decrease in Profits: {great_decrease}\n"
)

# Print the output
print(out_summary)



# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(out_summary)
