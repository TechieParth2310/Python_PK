# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password :- ")
size = len(password)

if(size<6):
    Strength = "Weak"
elif(size<=10):
    Strength = "Medium"
elif(size>10):
    Strength = "Strong"

print("Your Password Strength is",Strength)