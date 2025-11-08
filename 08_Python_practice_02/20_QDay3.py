# 📘 Problem Statement

# You are given a sentence (a string).
# You need to find which lowercase alphabets (a–z) are missing in that sentence.

# ✅ Ignore case (uppercase and lowercase treated same).
# ✅ Ignore spaces, digits, and special symbols.

S = input().strip().lower()
all_letters = set('abcdefghijklmnopqrstuvwxyz')
letters_in_S = {ch for ch in S if ch.isalpha()}
missing = sorted(all_letters-letters_in_S)
if len(missing) == 0:
    print("None")
else:
    print(''.join(missing))