# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = [-math.inf]

        def dfs(node):
            if node is None:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            max_sum[0] = max(max_sum[0], node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        dfs(root)

        return max_sum[0]