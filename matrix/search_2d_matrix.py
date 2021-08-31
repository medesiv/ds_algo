"""
Search 2D matrix:

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

"""

class Solution:
    
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
        
        
        
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
        
#         low, high = 0, m - 1
#         left, right = 0, n - 1
        
#         while low < high:      
#             mid = (high - low) // 2 + low
#             if target == matrix[mid][right]:
#                 return True
#             if target > matrix[mid][right]:
#                 low = mid + 1
#             else:
#                 high = mid
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if target == matrix[high][mid]:
#                 return True
#             elif target > matrix[high][mid]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
                
#         return False
