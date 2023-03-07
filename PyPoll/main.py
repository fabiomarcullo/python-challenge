import os
import csv

# Path to collect data from the Resources folder
electionpath = os.path.join("Resources/election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
candidate_votes = {}

# Read in the CSV file
with open(electionpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    next(csvreader)

    # Loop through rows in CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Add candidate to list of candidates, if not already in it
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0

        # Count votes for candidate
        candidate_votes[candidate] += 1

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes:,.0f}")
print("-------------------------")
for candidate in candidates:
    votes = candidate_votes[candidate]
    percent = (votes / total_votes) * 100
    print(f"{candidate}: {percent:.3f}% ({votes:,.0f})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save results to a text file
with open("Analysis/election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes:,.0f}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        votes = candidate_votes[candidate]
        percent = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percent:.3f}% ({votes:,.0f})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")