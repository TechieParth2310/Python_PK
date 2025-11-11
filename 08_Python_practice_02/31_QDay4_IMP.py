# 🧩 Q — Data Query (Simple Version)
# 📘 Problem

# Given details of n students —
# each record has: name, age, gender, grade

# You need to:
# 1️⃣ Print all names of students whose age > 20
# 2️⃣ Print the average grade of all female students (rounded to 2 decimals)


import sys

names = []          # stores names with age > 20
female_grades = []  # stores grades of all female students

for line in sys.stdin:
    name, age, gender, grade = line.strip().split()
    age = int(age)
    grade = float(grade)

    if age > 20:
        names.append(name)
    if gender.lower() == "female":
        female_grades.append(grade)

# Output 1: names whose age > 20
print(" ".join(names))

# Output 2: average of female grades (rounded to 2 decimals)
if female_grades:
    avg = sum(female_grades) / len(female_grades)
    print(f"{avg:.2f}")
else:
    print("0.00")
