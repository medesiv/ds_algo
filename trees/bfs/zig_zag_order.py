import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder2(self,root):
        if root is None:
            return []
        q = []
        res = []
        q.append(root)
        rev_order = False
        while len(q) > 0:
            temp = collections.deque()
            for _ in range(len(q)):
                node = q.popleft()
                if rev_order:
                    temp.appendleft()
                else:
                    temp.append()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(temp)
            rev_order = not rev_order
        return res

    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q = []
        res = []
        new_temp = []
        q.append(root)
        flag = False
        while len(q) > 0:
            temp = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            if flag:
                new_temp = temp[::-1]
                res.append(new_temp)
                flag = False
            else:
                res.append(temp)
                flag = True
        return res


        def zigzagLevelOrder3(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
            results = []

            if root is None:
                return results

            def dfs(node, level):
                if level == len(results):
                    results.append(collections.deque([node.val]))
                else:
                    if level % 2 == 0:
                        results[level].append(node.val)
                    else:
                        results[level].appendleft(node.val)

                for next_node in [node.left, node.right]:
                    if next_node is not None:
                        dfs(next_node, level + 1)

            # normal level order traversal with DFS
            dfs(root, 0)

            return results