import os
import csv
from datetime import date, datetime
from statistics import mean

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
        profit.append(float(row[index_profit]))
# print(date_string)
# print(profit)
        
# Total number of months included in the dataset
datetime = [datetime.strptime(date, "%b-%y") for date in date_string] # convert to datetime type

month_year_list = [(datetime.month, datetime.year) for datetime in datetime]
unique_months = set(month_year_list) # calculate number of unique values in list

print(f"Total Months: " + str(len(unique_months)))

# Net profit/loss over the period
profit_int = [int(string) for string in profit] # convert list of profits from string to integer in order to call sum()
net_profit = sum(profit_int)
print(f"Total: " + "${:,}".format(net_profit)) # format the integer as currency

# Sort the data by ascending date
data_tuple = zip(datetime, profit_int) # zip two lists into a tuple
sorted_tuple = sorted(data_tuple, reverse=False) # create a new sorted tuple

# Changes in "Profit/Losses" over the period
profit_change = []

beginning_value = sorted_tuple[0][1]
for element in sorted_tuple[1:]:
    change = element[1]-beginning_value
    beginning_value = element[1]
    profit_change.append(change)
average_profit_change = mean(profit_change) # average of "Profit/Losses" changes over the entire period
print(f"Average Change: " + str(average_profit_change))

# Greatest increase in profits (date and amount) during period
    # Take maximum of "Change" column

# Greatest decrease in profits during period
    # Take minimum of "Change" column
    
# Print the analysis to terminal

# Export a text file of results

