# 🧩 Q18 — Sort Words in Ascending / Descending Order
# 📘 Problem Statement

# You are given a string S containing words separated by spaces.
# Your task is to print the words sorted:
# 1️⃣ Once in ascending (A–Z) order
# 2️⃣ Once in descending (Z–A) order


S = input().strip()
words = S.split()
asc = sorted(words)
desc = sorted(words,reverse=True)
print("Ascneding: ",' '.join(asc))
print("Descending: ",' '.join(desc))
