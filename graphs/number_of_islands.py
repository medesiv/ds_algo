"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows_cnt = len(grid)
        cols_cnt = len(grid[0])
        num_islands = 0
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(r,c):
            if r<0 or c<0 or r>=rows_cnt or c>=cols_cnt or grid[r][c]=='0':
                return
            grid[r][c]='0'
            for d in dirs:
                dfs(r+d[0],c+d[1])
                        
        for r in range(rows_cnt):
            for c in range(cols_cnt):
                if grid[r][c]=='1':
                    dfs(r,c)
                    num_islands+=1
                    
        return num_islands