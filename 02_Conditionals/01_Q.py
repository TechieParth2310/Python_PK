# Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

userAge_str = input("Give me a User's Age :-  ")
userAge = int(userAge_str);
if userAge<13:
    print('Child')
elif userAge>12 and userAge<20:
    print('Teenager')
elif userAge>19 and userAge<60:
    print('Adult')
else:
    print("Senior")  