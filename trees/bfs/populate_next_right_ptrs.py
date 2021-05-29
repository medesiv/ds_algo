"""

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if root is None:
            return root
        q = []
        q.append(root)
        while len(q)>0:
            prev_node = None
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                if prev_node is not None:
                    prev_node.next = node
                prev_node = node
        return root
