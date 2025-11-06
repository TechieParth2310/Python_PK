
# Input
n = int(input())                     # Number of levels
levels = list(map(int, input().split()))  # Order in which levels are launched

# Initialize LIS array (each element can be a sequence of length 1)
lis = [1] * n

# Build LIS values
for i in range(1, n):               # start from 2nd element
    for j in range(0, i):           # check all elements before i
        if levels[i] > levels[j]:   # if increasing
            lis[i] = max(lis[i], lis[j] + 1)

# Answer is the max LIS length
print(max(lis))
