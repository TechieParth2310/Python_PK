# Q1 — Print Matrix in Normal Order

n, m = list(map(int,input().split()))
matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j],end=' ')
    print()

