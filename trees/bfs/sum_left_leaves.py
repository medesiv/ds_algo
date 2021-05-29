#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        q = []
        q.append(root)
        left_leaves_sum = 0
        while len(q) > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
                if self.is_leaf(node.left):
                    left_leaves_sum += node.left.val
            if node.right is not None:
                q.append(node.right)

        return left_leaves_sum

    def is_leaf(self, temp):
        return temp.left is None and temp.right is None