# 🔹 Q22 — Anagram Check
# Example:

# listen → silent
# triangle → integral

S1 = sorted(input().strip().lower())
S2 = sorted(input().strip().lower())
if(S1==S2):
    print("Anagram")
else:
    print("not Anagram")
