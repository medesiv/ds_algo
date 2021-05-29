import math

from node import Node


# class TreeNode():
#    def __init__(self, val=None, left_ptr=None, right_ptr=None):
#        self.val = val
#        self.left_ptr = left_ptr
#        self.right_ptr = right_ptr

def helper(root, low=-math.inf, high=math.inf):
    # if root is null return true

    if not root:
        return True

    if root.val < low or root.val > high:
        return False

    lbst = helper(root.left, low, root.val)
    rbst = helper(root.right, root.val, high)

    if lbst and rbst:
        return True
    else:
        return False


def isBST(root):
   return helper(root)


root = Node(300)
root.left = Node(200)
root.right = Node(400)
root.left.left = Node(100)
root.left.right = Node(400)
# root.right.left = Node(100)
# # root.right.right = Node(400)
# root.right.left.right = Node(400)

print(isBST(root))

"""
        300
   200       400
 100   400     
            

"""
