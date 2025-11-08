# 7.
# Given a list of numbers, find and print all Armstrong numbers from the list. An
# Armstrong number is a number that is equal to the sum of its own digits each raised
# to the power of the number of digits. For example, 153 is an Armstrong number
# because 13+53+33
# =153.

arr = list(map(int,input().split()))
found = False
for num in arr:
    digits = str(num)
    power = len(digits)
    arm = sum(int(d)**power for d in digits)
    if(num==arm):
        print(num,end=" ")
        found= True
    
if not found:
    print("No armstrong Number")



