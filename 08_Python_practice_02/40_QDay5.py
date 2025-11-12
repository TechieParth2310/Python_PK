# Q2 — Print Matrix Column-Wise

n, m = list(map(int,input().split()))
matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

for j in range(m):
    for i in range(n):
        print(matrix[i][j],end=' ')
    print()

