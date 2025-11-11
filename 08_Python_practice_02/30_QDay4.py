# 🧩 Q — Check if there exists a Subarray with Sum = 0

arr = list(map(int, input().split()))
n = len(arr)

prefix_sum = 0
seen = set()        # to store all prefix sums seen so far
found = False       # flag to mark if we find a 0-sum subarray

for i in range(n):
    prefix_sum += arr[i]     # add current element

    # Case 1: subarray from start
    if prefix_sum == 0:
        found = True
        break

    # Case 2: prefix_sum seen before (means in between sum became 0)
    if prefix_sum in seen:
        found = True
        break

    # Case 3: store prefix_sum for later checks
    seen.add(prefix_sum)

if found:
    print("Yes")
else:
    print("No")
