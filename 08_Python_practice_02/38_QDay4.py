# 🧩 Problem: Find the Winner Based on Votes
# 📘 Problem Description

# You are given:

# N = number of candidates

# M = number of locations

# A list of votes (each vote is a candidate’s name or symbol)

# You must:

# Count how many votes each candidate received

# Print the name of the candidate with the highest votes

# If there’s a tie, print "No Winner"

from collections import Counter

n, m = map(int, input().split())
votes = input().split()

# Step 1: Count frequency of votes
freq = Counter(votes)

# Step 2: Find the maximum vote count
max_votes = max(freq.values())

# Step 3: Check how many have this max value
winners = [name for name, count in freq.items() if count == max_votes]

# Step 4: Decision
if len(winners) > 1:
    print("No Winner")
else:
    print(winners[0])
