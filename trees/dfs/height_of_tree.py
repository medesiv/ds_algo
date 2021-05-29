class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        return max(map(self.maxDepth2, [root.left, root.right])) + 1 if root else 0

    def maxDepth3(self, root: TreeNode) -> int:
        if root is None:
            return 0

        lheight = self.maxDepth3(root.left)
        rheight = self.maxDepth3(root.right)

        return max(lheight, rheight) + 1


