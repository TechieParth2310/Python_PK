# 🧩 Problem: Permutations of a String
# 📘 Problem Summary. 

# You are given a string s (only uppercase letters).
# You have to find how many distinct permutations of the characters can be formed.

# Distinct = duplicates are not counted again.
# e.g., "AAB" → total 3 unique permutations (AAB, ABA, BAA)
# print values also 

from itertools import permutations

S = input().strip()

perm = permutations(S)

unique = sorted(set([''.join(p) for p in perm]))

for p in unique:
    print(p)