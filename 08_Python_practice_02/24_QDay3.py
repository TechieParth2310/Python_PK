# #🔹 Q24 — String Compression (Run-Length Encoding)

# 📘 Problem Statement

# Given a string, compress it so that repeated characters are replaced with
# character + count.

# Input:

# aaabbcddd


# Output:

# a3b2c1d3

S = input().strip()
n = len(S)

count = 1  # start counting from 1 for the first char

for i in range(1, n):
    if S[i] == S[i-1]:
        count += 1          # same char → increase count
    else:
        print(S[i-1],count,sep='',end='')  # print previous char and its count
        count = 1           # reset count for new char

# print the last group
print(S[-1],count,sep='',end='')
