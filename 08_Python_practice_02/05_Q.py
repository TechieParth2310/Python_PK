# 5. Fizz Buzz
# You have a list of integers. For each integer, you need to print a special word
# depending on its divisibility: print "ThreeFive" if the number is divisible by both 3 and
# 5, print "Five" if divisible only by 5, print "Three" if divisible only by 3, otherwise print
# the number itself.

# Sample Input:
# 5
# [1 3 5 15 16]
# Sample Output:
# 1 Three Five ThreeFive 16

int(input())
arr = list(map(int,input().split()))

for num in arr:
    if(num%3==0 and num%5==0):
        print("ThreeFive",end=" ")
    elif(num%3==0):
        print("Three",end=" ")
    elif(num%5==0):
        print("Five",end=" ")
    else:
        print(num,end=" ")
    