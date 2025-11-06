# Function to check if a string is palindrome
def is_palindrome(s):
    return s == s[::-1]

# Function to divide the string into 3 palindromes
def three_palindromes(word):
    n = len(word)

    # Try every possible way to split into 3 parts
    for i in range(1, n - 1):
        first = word[:i]
        if is_palindrome(first):
            for j in range(i + 1, n):
                second = word[i:j]
                third = word[j:]
                if is_palindrome(second) and is_palindrome(third):
                    # Print the three palindromes
                    print(first)
                    print(second)
                    print(third)
                    return
    print("Impossible")

# -------------------------------
# 🔹 Input section (TCS format)
word = input().strip()
three_palindromes(word)
