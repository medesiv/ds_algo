#Definition for a binary tree node.
"""
https://leetcode.com/problems/path-sum-iii/
https://leetcode.com/problems/path-sum-ii/

10
5 -3
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        Returns the count of the paths
        Using non local for res
        """
        res = 0
        if root is None:
            return res

        def count_path_sum(path):
            nonlocal res
            curr_sum = 0
            for i in range(len(path) - 1, -1, -1):
                curr_sum += path[i]
                if curr_sum == sum:
                    res += 1

        def helper(node, path):
            path.append(node.val)
            count_path_sum(path)
            if node.left is not None:
                helper(node.left, path)
            if node.right is not None:
                helper(node.right, path)
            path.pop()

        helper(root, [])

        return res

    def pathSum3(self, root: TreeNode, targetSum: int):
        """
        Adding the actual paths from root to leaf
        """
        res = []
        if root is None:
            return res

        def check_and_add_path_sum(path):
            curr_sum = 0
            for i in range(len(path) - 1, -1, -1):
                curr_sum += path[i]
            if curr_sum == targetSum:
                res.append(path[:])

        def helper(node, path):
            path.append(node.val)
            if node.left is None and node.right is None:
                check_and_add_path_sum(path[:])
            if node.right is not None:
                helper(node.right, path)
            if node.left is not None:
                helper(node.left, path)
            path.pop()

        helper(root, [])

        return res