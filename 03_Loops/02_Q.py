number = int(input("Enter the number :- "))
sum = 0;
while number>0:
    if(number%2==0):
        sum = sum+number
        print(f'Current Number is {number} and sum is {sum}')
    number-= 1

print(sum)    
