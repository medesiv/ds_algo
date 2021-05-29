"""
        1

  2              3

4   5          6    7

[[1,2,4],[1,2,5],[1,3,6],[1,3,7]]
"""

from trees.node import Node

root = Node(1)
root.construct_default_tree(root)

#preferred approach
def helper(root, path, res):
    if not root:
        return

    #print(id(path))
    if not root.left and not root.right:
        res.append(path[:])
    if root.left is not None:
        path.append(root.left.val)
        helper(root.left,path,res)
        path.pop()
    if root.right is not None:
        path.append(root.right.val)
        helper(root.right, path,res)
        path.pop()
    return res

def print_all_paths(root):
    return helper(root,[1],[])

print(print_all_paths(root))


