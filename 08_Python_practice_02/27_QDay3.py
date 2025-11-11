# 🧩 Q27 — Reverse the Sentence Without Reversing the Words
# 📘 Problem Statement

# Given a sentence, reverse the order of the words,
# but don’t reverse the characters inside the words.

S = input().strip()
words = S.split()
reversed_words = words[::-1]
print(' '.join(reversed_words))