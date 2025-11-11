# 🧩 Q25 — Longest Word in a Sentence

# 📘 Problem Statement

# Given a sentence, find the longest word in it.
# If there are multiple words with the same length, print the first one.

Sentence = input().strip()
words = Sentence.split()

max_len = 0 
longest_word = ""

for word in words:
    if(len(word)>max_len):
        max_len= len(word)
        longest_word=word
print(longest_word)

