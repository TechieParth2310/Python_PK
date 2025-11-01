# You are tasked with finding all numbers in a given range [n, m] that are prime and
# have a special property: the sum of their digits is also a prime number. For example,
# the number 23 is prime, and its digits sum to 5 (2+3), which is also prime. Your job is
# to print all such numbers between the given input range.

n,m = map(int,input().split())

def is_prime(num):
    if num<2:
        return False
    elif num>2:
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                return False
    return True

for num in range(n,m+1):
    if(is_prime(num)):
        digit_sum = sum(int(d) for d in str(num))
        # Alternate way :- 
        # digit_sum = 0
        # for d in str(num):
        #     digit_sum += int(d)
        if(is_prime(digit_sum)):
            print(num)

