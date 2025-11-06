# You have a list of students with their marks. Your task is to print the top K students
# ranked by their marks in descending order. If there are fewer than K students, print
# all.

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
# Alice: 85

# Explanation:
#  We want top 3 students (K=3) out of 5.
#  Students sorted by marks: Bob (92), David (90), Alice (85), Eva (88), Charlie
# (78).
#  Top 3 printed in order: Bob, David, Alice.

# Read K and N
k, n = map(int, input().split())

students = []
for _ in range(n):
    marks, name = input().split()
    marks = int(marks)
    students.append((marks, name))

# Sort by marks descending, then by name ascending
students.sort(key=lambda x: (-x[0], x[1]))

# Print top K students
for i in range(min(k, n)):
    print(f"{students[i][1]}: {students[i][0]}")
