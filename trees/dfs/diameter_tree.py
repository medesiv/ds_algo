# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree2(self, root):
        """
        From leet code
        """

        self.ans = 1

        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = [0]

        if root is None:
            return 0

        def helper(node, height):
            height = 0
            dia = 0
            if node.left is None and node.right is None:
                return 0
            if node.left is not None:
                left_height = helper(node.left, height)
                dia += 1 + left_height
                height = max(height, 1 + left_height)
            if node.right is not None:
                right_height = helper(node.right, height)
                dia += 1 + right_height
                height = max(height, 1 + right_height)

            diameter[0] = max(diameter[0], dia)

            return height

        helper(root, 0)
        return diameter[0]

