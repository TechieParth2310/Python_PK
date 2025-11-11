# Subarray with Target Sum : - 

# arr = list(map(int,input().split()))
# target = int(input())
# n = len(arr)

# for i in range(n):
#     for j in range(i,n):
#         subarr = arr[i:j+1]
#         if target == sum(subarr):
#             print((i,j),end=' ')


from collections import defaultdict

arr = list(map(int, input().split()))
target = int(input())

prefix_map = defaultdict(list)   # stores prefix_sum -> [indices]
curr_sum = 0
results = []

for i in range(len(arr)):
    curr_sum += arr[i]

    # Case 1: subarray starts from index 0
    if curr_sum == target:
        results.append((0, i))

    # Case 2: check if there's a previous prefix that makes target
    need = curr_sum - target
    if need in prefix_map:
        for start in prefix_map[need]:
            results.append((start + 1, i))

    # Store current prefix sum for future use
    prefix_map[curr_sum].append(i)

print(results)
