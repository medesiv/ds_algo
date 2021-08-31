"""
Leetcode 64

Input: grid = 
[[1,3,1],
[1,5,1],
[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

"""

def minPathSum(grid):
    n = len(grid[0])
    m = len(grid)
    path = []
    table = [[0 for j in range(n)] for i in range(m)]
    table[0][0]= grid[0][0]
    #row 0
    for col in range(1,n):
        table[0][col]= table[0][col-1]+grid[0][col]
    #col 0
    for row in range(1,m):
        table[row][0]= table[row-1][0]+grid[row][0]

    for row in range(1,m):
        for col in range(1,n):
        	table[row][col] = grid[row][col] + min(table[row-1][col],table[row][col-1])
    print(table[-1][-1])
    return table[m-1][n-1]




grid = [[1,3,1],[1,5,1],[4,2,1]]
minPathSum(grid)