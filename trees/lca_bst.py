#Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root
        while node:
            parent = node
            if p.val > parent.val and q.val > parent.val:
                node = root.left
            elif p.val < parent.val and q.val < parent.val:
                node = root.right
            else:
                return node

class Solution:

    def lowestCommonAncestor(self, root, p, q):
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root