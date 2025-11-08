# 🧩 Question 3 — Sum of Unique Elements
# 📘 Problem:

# You are given a list of integers.
# Find the sum of all numbers that appear exactly once in the list.

# sol 1:- 

# arr = list(map(int,input().split()))
# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num]=1

# sum =0

# for key in freq:
#     if freq[key]==1:
#         sum = sum+key

# print(sum)

# sol 2:- 

from collections import Counter


arr = list(map(int,input().split()))
freq = Counter(arr)

sum_unique = sum(k for k,v in freq.items() if v==1)

print(sum_unique)
