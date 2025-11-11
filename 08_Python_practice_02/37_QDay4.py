# 🧩 Problem: Find LCM Using Formula
# 📘 What is LCM?

# LCM (Least Common Multiple) of two numbers A and B is the smallest positive integer that is divisible by both A and B.

# Example:
# LCM(8, 10) = 40
# (because 40 is the first number divisible by both 8 and 10)

import math

a, b = map(int, input().split())

lcm = (a * b) // math.gcd(a, b)
print(lcm)

