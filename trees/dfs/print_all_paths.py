#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def binaryTreePaths(self, root: TreeNode):
        res = []
        if root is None:
            return []

        def helper(slate, root):
            slate.append(str(root.val))
            if root.left is None and root.right is None:
                res.append("->".join(slate[:]))
            if root.left is not None:
                helper(slate, root.left)
            if root.right is not None:
                helper(slate, root.right)
            slate.pop()

        helper([], root)

        return res