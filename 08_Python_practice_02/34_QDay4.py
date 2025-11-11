# 🧩 Problem: Remove Duplicate Words and Print in Sorted Order
# 📘 Problem Description

# You’re given a single line containing multiple words (space-separated).
# You need to:

# Remove all duplicate words

# Print the unique words:

# First in ascending (A→Z) order

# Then in descending (Z→A) order

# ⚠️ Note:

# Case-sensitive → "Apple" and "apple" are different words.

# You can use Python’s set() to remove duplicates.


# Step 1: Take input
words = input().split()

# Step 2: Remove duplicates
unique_words = set(words)

# Step 3: Sort ascending
asc = sorted(unique_words)

# Step 4: Sort descending
desc = sorted(unique_words, reverse=True)

# Step 5: Print
print(" ".join(asc))
print(" ".join(desc))
