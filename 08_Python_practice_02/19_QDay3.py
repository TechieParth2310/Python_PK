# 🧩 Q19 — Student Records (ASCII Average)
# 📘 Problem Statement

# You are given a student’s name as a string.
# Your task is to:
# 1️⃣ Find the ASCII value of each character,
# 2️⃣ Compute their average,
# 3️⃣ Print that average value (as an integer).

S= input().strip()

Ascii = sum(ord(ch)for ch in S)
N = len(S)
avg = Ascii//N
print((avg))
