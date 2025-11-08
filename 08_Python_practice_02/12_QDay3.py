# 🧩 Question 12 — Sum of Cubes in a Range
# 📘 Problem Statement

# Given two integers L and R,
# find the sum of cubes of all numbers between L and R (both inclusive).

L,R = map(int,input().split())
ans = sum(i**3 for i in range(L,R+1))
print(ans)