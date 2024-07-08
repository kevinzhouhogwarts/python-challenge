import os
import csv
from datetime import date, datetime
from statistics import mean

# Encountered file not found error, then discovered the working directory was the parent directory (python-challenge), not \python-challenge\PyBank\.
# Tried copying code to a new .py file but encountered same error. Maybe because I created \PyBank\ folder after starting work on original main.py.
# Resorted to using below two lines to explicitly specify the working directory
script_dir = os.path.dirname(os.path.abspath(__file__)) # locate directory of this file
os.chdir(script_dir) # change working directory to file directory

# Read the csv file
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
print("CSV Path:", budget_data_csv)

with open(budget_data_csv) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    csv_header = next(csv_reader)

    net_profit = 0
    unique_months_list = [] # list to hold unique date strings
    profit_change_list = [] # list to hold change of profit between months
    starting_profit = 0 # hold profit/loss of the previous month during iteration of profit changes
    greatest_increase = {"amount": 0, "month_year": "Jan-20"}
    greatest_decrease = {"amount": 0, "month_year": "Jan-20"}
    results = [] # list to hold printed text results

    for index, row in enumerate(csv_reader):
        # calculate the net profit
        profit = float(row[1]) # extract the profit from second column of csv
        net_profit = net_profit + profit # add profit to net profit

        # calculate the number of unique months
        month_year = row[0]
        if month_year not in unique_months_list:
            unique_months_list.append(month_year) # if datetime does not appear in list, then append
        else:
            pass # otherwise, do nothing
        
        # create list of profit changes
        if index == 0:
            profit_change = 0
        else:
            profit_change = float(row[1]) - starting_profit
            profit_change_list.append(profit_change)
        starting_profit = float(row[1])

        # compare profit changes to find min and max
        if profit_change > greatest_increase["amount"]:
            greatest_increase["amount"] = profit_change
            greatest_increase["month_year"] = month_year
        else:
            pass
        
        if profit_change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = profit_change
            greatest_decrease["month_year"] = month_year
        else:
            pass

def print_append(text): # define new function to both print to terminal and append printed text to list
    print(text)
    results.append(text + "\n")

print_append(f"Financial Analysis")
print_append('-' * 15)

unique_months = len(unique_months_list)
print_append(f"Total Months: " + str(unique_months))

print_append(f"Total Profit: " + "${:,}".format(net_profit)) # format the integer as currency

average_profit_change = mean(profit_change_list)
print_append(f"Average Change: " + str(average_profit_change))

print_append(f"Greatest Increase in Profits: " + str(greatest_increase["amount"]) + " in " + str(greatest_increase["month_year"]))

print_append(f"Greatest Decrease in Profits: " + str(greatest_decrease["amount"]) + " in " + str(greatest_decrease["month_year"]))

# export list of printed text to text file
output_path = os.path.join("..", "analysis", "profit_results.txt")
with open(output_path, "w") as file:
    file.writelines(results)