# 🧩 Question 10 — Prime + Sum of Digits Prime
# 📘 Problem Statement:

# You are given two integers n and m.
# You need to print all numbers between n and m (inclusive) that are:
# 1️⃣ Prime numbers, and
# 2️⃣ The sum of their digits is also prime.



def Isprime(N):
    if N<1:
        return False
    elif N==1:
        return False
    elif N==2:
        return True
    
    for i in range(2,int((N**(0.5)))+1):
            if(N%i==0):
                return False
    return True

n,m = map(int,input().split())
for num in range(n,m+1):
    if Isprime(num):
        sum_d = sum(int(d) for d in str(num))
        if(Isprime(sum_d)):
            print(num,end=' ')
