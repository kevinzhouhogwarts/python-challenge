import os
import csv
from datetime import date, datetime
from statistics import mean

# Read the csv file
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")
print("Current Working Directory:", os.getcwd())

with open(budget_data_csv) as budget_data:
    csv_reader = csv.reader(budget_data, delimiter=",")

    csv_header = next(csv_reader)

    date_string = []
    profit = []

    index_date = csv_header.index("Date")
    index_profit = csv_header.index("Profit/Losses")

    for row in csv_reader: # Pass all values in the two columns to new lists
        date_string.append(row[index_date])
        profit.append(float(row[index_profit]))

print(f"Financial Analysis")
print('-' * 15)
        
# Find the total number of months
datetime = [datetime.strptime(date, "%b-%y") for date in date_string] # convert to datetime type
month_year_list = [(datetime.month, datetime.year) for datetime in datetime] # convert to list of month & year tuples
unique_months = set(month_year_list) # calculate number of unique tuples in list

print(f"Total Months: " + str(len(unique_months)))

# Find the net profit/loss
profit_int = [int(string) for string in profit] # convert list of profits from string to integer in order to call sum()
net_profit = sum(profit_int)
print(f"Total: " + "${:,}".format(net_profit)) # format the integer as currency

# Sort the data by ascending date (not needed with this csv though)
data = zip(datetime, profit_int) # combine two lists
sorted = sorted(data, reverse=False)

# Changes in "Profit/Losses"
profit_change = [0] # set change in profit of first month to zero since there is no prior data

start_value = sorted[0][1] # sets beginning profit to profit value from the first row
for value in sorted[1:]: # iterates over all rows starting from row index 1
    change = value[1]-start_value
    start_value = value[1] # after calculating the profit change, update the begining profit for the next iteration
    profit_change.append(change) # add profit change to list
average_profit_change = mean(profit_change)
print(f"Average Change: " + str(average_profit_change))

# Greatest increase in profits (date and amount) during period
greatest_increase = max(profit_change)
greatest_increase_index = profit_change.index(greatest_increase)
print(f"Greatest Increase in Profits: " + str(greatest_increase) + " in " + str(sorted[greatest_increase_index][0].strftime("%b-%Y")))

# Greatest decrease in profits during period
greatest_decrease = min(profit_change)
greatest_decrease_index = profit_change.index(greatest_decrease)
print(f"Greatest Decrease in Profits: " + str(greatest_decrease) + " in " + str(sorted[greatest_decrease_index][0].strftime("%b-%Y")))

# Export a text file of results
pybank