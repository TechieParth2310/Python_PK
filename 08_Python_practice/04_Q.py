import math 
def uniquePaths(m,n):
    return math.comb(m+n-2,n-1)

print(uniquePaths(10,10))