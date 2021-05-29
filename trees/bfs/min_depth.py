

def min_depth(root):
    level = 0
    if root is None:
        return level
    q = []
    q.append(root)
    while len(q) > 0:
        level += 1
        for _ in range(len(q)):
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            if node.left is None and node.right is None:
                return level


def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = []
    if root is not None:
        queue.append(root)

    depth = 0
    while len(queue)>0:
        depth+=1
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    return depth
