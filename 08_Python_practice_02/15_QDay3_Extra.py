# Printing Subarray:-

arr = list(map(int,input().split()))
n = len(arr)
for i in range(n):
    for j in range(i,n):
        subarray = arr[i:j+1]
        print(subarray)

# # Input
# n = int(input())
# arr = list(map(int, input().split()))

# # Generate and print each subarray + OR result
# for i in range(n):
#     curr_or = 0
#     for j in range(i, n):
#         curr_or |= arr[j]            # update OR value
#         subarray = arr[i:j+1]        # slice
#         print(f"Subarray: {subarray}  →  OR = {curr_or}")
