from trees.node import Node

root = Node(5)
root.left = Node(5)
root.right = Node(5)
root.left.left = Node(5)
root.left.right = Node(5)
root.right.left = Node(4)
root.right.right = Node(5)

"""

        5
        
    5       4

5   5       5   5

"""


def helper(root, count):
    if root is None:
        return True, count

    left, count = helper(root.left, count)
    right, count = helper(root.right, count)

    if left == False or right == False:
        return False, count
    if root.left and root.val != root.left.val:
        return False, count
    if root.right and root.val != root.right.val:
        return False, count

    count += 1
    return True, count


def uni_val_counter(root):
    _, result = helper(root, 0)
    return result

print(uni_val_counter(root))