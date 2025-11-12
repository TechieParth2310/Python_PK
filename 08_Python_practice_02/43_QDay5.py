m,n = list(map(int,input().split()))
matrix = []

for i in range(m):
    rows = list(map(int,input().split()))
    matrix.append(rows)

result = []

for i in range(m):
    if i%2==0:
        result.extend(matrix[i])
    else:
        result.extend(matrix[i][::-1])
print(*result)
