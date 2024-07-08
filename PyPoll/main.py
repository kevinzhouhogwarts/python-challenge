import os
import csv

# Same error as noted in PyBank's main.py, despite creating PyPoll's main.py after creating \PyPoll\ folder
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Read the csv file
election_data_csv = os.path.join("..", "Resources", "election_data.csv")
# print("CSV Path:", election_data_csv)
# print(os.path.abspath(election_data_csv))

with open(election_data_csv) as election_data:
    csv_reader = csv.reader(election_data, delimiter=",")

    csv_header = next(csv_reader)

    candidate_count = {} # initialize dictionary to store each candidate and their individual vote count
    total_votes = 0 # intialize integer variable to store total number of votes

    for vote in csv_reader: # loop through all rows in the data
        total_votes += 1 # increment the number of total votes by one
        candidate = vote[2] # extract the name of the candidate
        if candidate in candidate_count:
            candidate_count[candidate] += 1 # if found, increment its count of votes by one
        else:
            candidate_count[candidate] = 1 # if not found, add the candidate by setting its count to zero

# print the results

results = [] # define list to hold the printed results

def print_append(text): # define a new function that performs printf and append to the results list at the same time
    print(text)
    results.append(text + "\n")

print_append(f"Election Results")
print_append('-' * 15)

for candidate in candidate_count:
    percent_vote = candidate_count[candidate] / total_votes * 100
    print_append(f"{candidate}: {candidate_count[candidate]} ({percent_vote:.2f}%)")

print_append(f"Total number of votes: {total_votes}")

winner = max(candidate_count, key=candidate_count.get)
print_append(f"Winner: {winner}")

# export to text file
output_path = os.path.join("..", "analysis", "election_results.txt")
with open(output_path, "w") as file:
    file.writelines(results)
    