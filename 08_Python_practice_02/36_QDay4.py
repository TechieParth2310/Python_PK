# Std Deviation of Array :- 

arr = list(map(int,input().split()))

n = len(arr)

mean = sum(arr)/n

std = sum((i-mean)**2 for i in arr)

ans = (std/n)**0.5

print(f'{ans:.2f}')