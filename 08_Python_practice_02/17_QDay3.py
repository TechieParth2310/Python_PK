# 🧩 Q17 — Shift Letters / Digits by Value
# 📘 Problem Statement

# You are given a string S containing letters and digits.
# You have to shift each character by a given integer K positions forward in its respective group.

# 👉 Rules:

# If it’s a lowercase letter, shift within 'a' to 'z'.

# If it’s an uppercase letter, shift within 'A' to 'Z'.

# If it’s a digit, shift within '0' to '9'.

# If the shift goes past 'z' or '9', wrap around (circular shift).


S = input().strip()
K = int(input())

result = ""

for ch in S :
    if 'A'<=ch<='Z':
        shift = chr((ord(ch)-ord('A')+K)%26+ord('A'))
    elif 'a'<=ch<='z':
        shift = chr((ord(ch)-ord('a')+K)%26+ord('a'))
    elif '0'<=ch<='9':
        shift = chr((ord(ch) - ord('0') + K) % 10 + ord('0'))
    else:
        shift = ch
    result = result+shift
print(result)