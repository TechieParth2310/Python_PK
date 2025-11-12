
# 🧩 Q4 — Sum of Diagonals of a Square Matrix

n,m = list(map(int,input().split()))
matrix = []

for i in range(n):
    rows = list(map(int,input().split()))
    matrix.append(rows)

Primary = sum(matrix[i][i] for i in range(n))
Secondary = sum(matrix[i][n-i-1] for i in range(n))

print(Primary)
print(Secondary)