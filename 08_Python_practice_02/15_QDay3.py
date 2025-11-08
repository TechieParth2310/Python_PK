# 🧩 Q15 — Bitwise OR of Subarrays
# 📘 Problem Statement

# Given an array of integers,
# you have to find how many distinct values you can get
# by performing bitwise OR on all possible subarrays of that array.

n = int(input())
arr = list(map(int,input().split()))
unique_Or = set()

for i in range(n):
    curr_or = 0
    for j in range(i,n):
        curr_or = curr_or | arr[j]
        unique_Or.add(curr_or)
print(len(unique_Or))

