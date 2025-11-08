# 🧩 Q16 — Change Case (Swapcase)
# 📘 Problem Statement

# You are given a string S containing both uppercase and lowercase letters.
# You have to swap the case of each character:

# Uppercase letters → lowercase

# Lowercase letters → uppercase

# code :-

# S = input().strip()

# result = ""
# for ch in S:
#     if ch.islower():
#         result = result+ch.upper()
#     if ch.isupper():
#         result = result+ch.lower()
#     else:
#         result = result+ch
# print(result)

print(input().strip().swapcase())