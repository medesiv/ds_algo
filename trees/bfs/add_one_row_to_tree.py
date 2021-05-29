# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        q = []
        if d <= 1:
            new_node = TreeNode(v, root)  # [4,2,6]
            return new_node
        level = 0
        q.append(root)
        while len(q) > 0 and level<d:
            level += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                if level == d - 1:
                    new_node_left = TreeNode(v, node.left)
                    node.left = new_node_left
                    new_node_right = TreeNode(v, None,node.right)
                    node.right = new_node_right
        return root