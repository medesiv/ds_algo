# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        q = []
        res = []
        q.append(root)
        while len(q)>0:
            for _ in range(len(q)):
                node = q.pop(0)
                for next_node in [node.left,node.right]:
                    if next_node is not None:
                        q.append(next_node)
            res.append(node.val)
        return res

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        q = []                  #[1,2,3,null,5,null,4]
        res = []
        q.append(root)
        temp = []
        while len(q)>0:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            res.append(temp.pop())
        return res






