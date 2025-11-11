# 🧩 Problem: Permutations of a String
# 📘 Problem Summary

# You are given a string s (only uppercase letters).
# You have to find how many distinct permutations of the characters can be formed.

# Distinct = duplicates are not counted again.
# e.g., "AAB" → total 3 unique permutations (AAB, ABA, BAA)

from math import factorial
from collections import Counter

s = input().strip()

# Step 1: total characters
n = len(s)

# Step 2: frequency count of each character
freq = Counter(s)

# Step 3: compute denominator = product of factorials of frequencies
denominator = 1
for count in freq.values():
    denominator *= factorial(count)

# Step 4: apply formula
ans = factorial(n) // denominator

print(ans)
