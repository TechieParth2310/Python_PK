# Missing Number 

N=int(input("Enter Count N : "))
arr = list(map(int,input("Enter space-separated elements: ").split()))
sum = 0 
for num in arr:
    sum = sum+num
print(sum)
total = (N*(N+1))//2
print("Missing number: ",int(total-sum))
