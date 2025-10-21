# 10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

def factorial(num):
    if num==0:
        return 1
    if num==1:
        return 1
    ans =num*factorial(num-1)
    return ans

print(factorial(6))
