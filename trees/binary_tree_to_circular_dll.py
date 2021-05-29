from node import Node

"""
            4
    2               5
1     3


1===2===3==4==5
||============||

"""
import math


class CircularNode:

    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val



def convert_bt_to_circular_dll(root):
    #Create a sentinel
    sentinel = CircularNode(-math.inf)

    #Create a predecessor node
    predecessor = CircularNode(-math.inf)

    #Set the sentinel as predecessor
    sentinel = predecessor

    def wire_up_dll(node):
        nonlocal predecessor
        # traverse left
        if node.left is not None:
            wire_up_dll(node.left)
        # wire up the node and predecessor
        node.left = predecessor
        predecessor.right = node
        # set this node as predecessor
        predecessor = node
        # traverse right

        if node.right is not None:
            wire_up_dll(node.right)

    if root is None:
        return

    #recurse
    wire_up_dll(root)

    #connect the last item in tree to first node (sentinel sucessor)
    predecessor.right = sentinel.right
    sentinel.right.left = predecessor

    #return the first node
    return sentinel.right




root = Node(4)
root.construct_default_tree(root)
root.print_level_tree(root)
print("\n")
cll = convert_bt_to_circular_dll(root)
temp = cll
while temp.right.val != 7:
    print("\t",temp.val,"==",end='')
    temp = temp.right


