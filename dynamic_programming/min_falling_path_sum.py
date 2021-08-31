class Solution:
    """
    Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
    Output: 13
    Explanation: There are two falling paths with a minimum sum underlined below:
    [[2,1,3],      [[2,1,3],
     [6,5,4],       [6,5,4],
     [7,8,9]]       [7,8,9]]
    """
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(1, m):
            for col in range(n):
                if col == 0:
                    matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col+1])
                elif col == n - 1:
                    matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1])
                else:
                    matrix[row][col] += min(matrix[row-1][col], matrix[row-1][col-1], matrix[row-1][col+1])
        
        return min(matrix[-1])