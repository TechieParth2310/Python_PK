# Sum of all elements in matrix :- 

n,m = list(map(int,input().split()))
matrix = []

for i in range(n):
    rows = list(map(int,input().split()))
    matrix.append(rows)
    
total = sum(sum(row)for row in matrix)
    

 
# for i in range(n):
#     for j in range(m):
#         sum += matrix[i][j]
print(total)