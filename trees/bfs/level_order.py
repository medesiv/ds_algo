from node import Node

def level_order_queue(root):
    q = []
    if root is None:
        return
    q.append(root)
    while len(q) > 0:
        print(q[0].val)
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def level_order_recursion(root):
    h = height(root)
    print("height is",h)
    if root is None:
        return
    else:
        for d in range(1,h+1):
            print_level(root,d)

def height(root):

    return height_helper(root)

def height_helper(root):
        lheight=rheight = 0
        if root is None:
            return 0

        lheight = height_helper(root.left)

        rheight = height_helper(root.right)

        if lheight > rheight:
             return lheight + 1
        else:
            return rheight + 1


def print_level(root,level):
        if level == 1:
            print(root.val)
        elif level>1:
            if(root.left is not None):
                print_level(root.left,level-1)
            if(root.right is not None):
                print_level(root.right,level-1)


root = Node(1)
root.construct_default_tree(root)

print("\nLevel traversal(Using queue) of binary tree is")
level_order_queue(root)

print("\nLevel traversal(Using recursion) of binary tree is")
level_order_recursion(root)
"""
            1
    2           3
   4 5

"""