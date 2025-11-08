# 🔹 Q21 — Palindrome Check

S = input().strip().lower()
if S == S[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
