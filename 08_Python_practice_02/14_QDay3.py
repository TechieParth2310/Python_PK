# 🧩 Q14 — Multiplication Table & Sum
# 📘 Problem Statement

# Given an integer N,
# you need to print its multiplication table from 1 to 10,
# and at the end, print the sum of all products.

N = int(input())
Total = 0
for i in range(1,11):
    Total = sum(N*i for i in range(1,11))
    print(f'{N}X{i} = {N*i}')
print(Total)