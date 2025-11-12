m,n = list(map(int,input().split()))
matrix = []
minimum = 129761432

for i in range(m):
    rows = list(map(int,input().split()))
    matrix.append(rows)

for i in range(m):
    for j in range(n):
        minimum = min(minimum,matrix[i][j])

print(minimum)