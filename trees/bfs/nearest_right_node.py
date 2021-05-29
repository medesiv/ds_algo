"""

            1
    2               3

        4          5    6

Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.
https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

"""
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
    "Most intuitive solution"
    q = []
    if root is None:
        return
    q.append(root)
    while len(q) > 0:
        level_size = len(q)
        for i in range(len(q)):
            node = q.pop(0)

            if node == u:
                # If the node is the last element in the level
                if i == level_size - 1:
                    return None
                else:
                    return q[0]
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    # If we didn't find the node
    return None


def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
    q = []
    if root is None:
        return
    q.extend([root, None])
    while q:
        node = q.pop(0)

        if node == u:
            return q[0]

        if node:
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        else:
            if q:
                q.append(None)

    # [1,None, 2, 3, [None, 4,5,6],None]


    def findNearestRightNode2Queues(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if root is None:
            return []

        next_level = deque([root,])
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()

                if node == u:
                    return curr_level.popleft() if curr_level else None
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = None
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

print(findNearestRightNode(root,Node(4)))