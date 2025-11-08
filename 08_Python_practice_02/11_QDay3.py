# --------------------------------------------
# 🧩 Q11 — Unique Paths in a Grid
# --------------------------------------------
# Problem:
# You're in the top-left corner of an m×n grid.
# You can only move RIGHT or DOWN.
# Find the total number of unique paths
# to reach the bottom-right corner (m-1, n-1).
# --------------------------------------------

# ✅ Step 1: Take inputs
# m = number of rows
# n = number of columns

m, n = map(int, input().split())

# ✅ Step 2: Create a 2D DP table (list of lists)
# ways[i][j] will store how many unique paths reach cell (i, j)

ways = [[0] * n for _ in range(m)]

# ✅ Step 3: Base Case Initialization
# First row → only 1 way (go right)
# First column → only 1 way (go down)

for i in range(m):
    ways[i][0] = 1       # 1 way to move straight down
for j in range(n):
    ways[0][j] = 1       # 1 way to move straight right

# ✅ Step 4: Fill the DP table using relation:
# ways[i][j] = ways[i-1][j] + ways[i][j-1]
# (paths from top + paths from left)

for i in range(1, m):
    for j in range(1, n):
        ways[i][j] = ways[i-1][j] + ways[i][j-1]

# ✅ Step 5: The bottom-right cell (m-1, n-1)
# contains the total number of unique paths

print(ways[m-1][n-1])

# --------------------------------------------
# ✅ Example:
# Input: 3 3
# Grid looks like:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
#
# DP table after filling:
# 1 1 1
# 1 2 3
# 1 3 6
#
# Output: 6
# --------------------------------------------

# By using Formula :-

# import math

# m, n = map(int, input().split())
# paths = math.comb(m + n - 2, m - 1)
# print(paths)
