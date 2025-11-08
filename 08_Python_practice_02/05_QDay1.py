# 🧩 Question 5 — Top K Students by Marks
# 📘 Problem Statement:

# You are given N students, each with:

# their marks (integer), and

# their name (string).

# You also get an integer K — you need to print the top K students based on marks, in descending order.

# Sample Input:
# 3 5
# 85 Alice
# 92 Bob
# 78 Charlie
# 90 David 
# 88 Eva

# Sample Output:
# Bob: 92
# David: 90
# Eva: 88

K,N = map(int,(input().split()))
students = []

for _ in range(N):
    marks,name = input().split()
    students.append((int(marks),name))

students.sort(reverse=True)

for i in range(K):
    print(f"{students[i][1]}:{students[i][0]}")


# students.sort(key=lambda x: (-x[0], x[1])) --> remember 
