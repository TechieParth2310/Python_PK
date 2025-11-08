# Missing Number 

N=int(input("Enter Count N : "))
arr = list(map(int,input("Enter space-separated elements: ").split()))

actual_sum = (N*(N+1))/2
given_sum = sum(arr)
print(int(actual_sum-given_sum))
1