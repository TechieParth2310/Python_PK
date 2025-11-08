# 🧩 Question 6 — Character Frequency Threshold (≥ p)
# 📘 Problem Statement:

# You are given:

# A string s (all lowercase letters)

# An integer p (the frequency threshold)

# You must find the first character in the string whose frequency
# is greater than or equal to p.

# 👉 If multiple characters qualify, print the alphabetically smallest one.
# 👉 If no character meets the condition, print nothing (empty output).


from collections import Counter

s = input().strip()
p = int(input())

freq = Counter(s)

candidates = [ch for ch,count in freq.items() if count>=p]

ans = min(candidates)

for ch in s:
    if ch==ans:
        print(ch)
        break
