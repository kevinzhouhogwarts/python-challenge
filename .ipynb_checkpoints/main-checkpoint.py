import os
import csv
from datetime import date, datetime

# Read the csv file
budget_data_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    csv_header = next(csv_reader)
    # print(csv_header)

    # Pass all values in the two columns to new lists
    date_string = []
    profit = []

    index_date = csv_header.index("Date")
    index_profit = csv_header.index("Profit/Losses")

    for row in csv_reader:
        date_string.append(row[index_date])
        profit.append(row[index_profit])
# print(date_string)
# print(profit)
        
# Total number of months included in the dataset
# Get month from date by first converting date string to datetime type
datetime_list = [datetime.strptime(date, "%b-%y") for date in date_string]
# Get number of unique values in month
month_year_list = [(datetime.month, datetime.year) for datetime in datetime_list]
unique_months = set(month_year_list)
print(month_year_list)
print(f"Number of unique months in the dataset " + str(len(unique_months)))

# Net profit/loss over the period
    # Sum all values in Profit/Losses
net_profit = profit.sum()

# Changes in "Profit/Losses" over the period
    # Add a new column

    # Use loop to populate column

# Average of "Profit/Losses" changes over the period
    # Take average of new "Change" column

# Greatest increase in profits (date and amount) during period
    # Take maximum of "Change" column

# Greatest decrease in profits during period
    # Take minimum of "Change" column
    
# Print the analysis to terminal

# Export a text file of results

