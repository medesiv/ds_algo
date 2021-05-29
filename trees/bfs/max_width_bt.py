#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q, result = [], []
        q.append([root,1])
        while len(q)>0:
            first = None
            last = None
            for _ in range(len(q)):
                (node,id) = q.pop(0)
                if node.left is not None:
                    q.append([node.left, 2*id])
                if node.right is not None:
                    q.append([node.right, 2*id+1])
                last = id
                if first is None:
                    first = id
            result.append(last-first+1)
        return max(result)