# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        seen = set()
        def helper(root, k):
            if root is None:
                return 
            
            if k - root.val in seen:
                return True
            
            if root.val not in seen:
                seen.add(root.val)
                    
            left = helper(root.left, k)
            right = helper(root.right, k)
            
            if left or right:
                return True
       
            
                
        return helper(root, k)
        print(seen)
