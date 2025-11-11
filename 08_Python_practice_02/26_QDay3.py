# --------------------------------------------
# 🧩 Q26 — Longest Palindromic Word in a Sentence
# --------------------------------------------

sentence = input().strip().lower()          # lowercase for uniform check
words = sentence.split()                    # split into list of words

longest_palindrome = ""
max_len = 0

for word in words:
    if word == word[::-1]:                  # check palindrome
        if len(word) > max_len:             # check if longer
            max_len = len(word)
            longest_palindrome = word

if longest_palindrome == "":
    print("None")
else:
    print(longest_palindrome)
