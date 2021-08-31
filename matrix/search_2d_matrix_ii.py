class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0 or n == 0:
            return False
        
        row = m - 1
        col = 0
        
        while col < n and row >= 0:
            if matrix[row][col]  > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        
        