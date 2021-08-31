class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = []
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges +=1        
        
        if fresh_oranges == 0:
            return 0
        
        time = -1 #When we visit the first node then time must be 0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        
        while len(q) > 0:
            time +=1 #time 0 for first node
            size = len(q)
            for i in range(size):
                sr, sc = q.pop(0)
                for d in dirs:
                    nr = sr + d[0]
                    nc = sc + d[1]
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh_oranges -=1

        if fresh_oranges == 0:
            return time
        else:
            return -1              
        
        