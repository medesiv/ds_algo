"""
LC 120

min path sum on a triangle

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above)

"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)

        # copy the triangle to table
        table = [[0 for cols in range(rows+1)] for rows in range(m)]
        table[0][0] = triangle[0][0]
        
        #filling base cases for left most col and right most col in each row
        for row in range(1,m):
            table[row][0]=table[row-1][0]+triangle[row][0]
            table[row][row]=table[row-1][row-1]+triangle[row][row]
        
        
        for row in range(2,m):
            for col in range(1,row):
                table[row][col]= min(table[row-1][col],table[row-1][col-1])+triangle[row][col]
                
        #answer will be min of all values in last row        
        return min(table[-1])
        