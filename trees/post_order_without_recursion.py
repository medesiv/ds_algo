"""
                100
       200             300
400         500
    450
 50    40
"""
from node import Node

root = Node(100)
root.left = Node(200)
root.right = Node(300)
root.left.left = Node(400)
root.left.right = Node(500)

"""

100 

300
200         100 
============================

            300
200         100
============================
            
            200
500         300
400         100
"""

def post_order_without_recursion(root):
    stack = []
    stack2 = []
    if not root:
        return root
    else:
        curr = root
        stack.append(curr)
        while stack:
            curr = stack.pop()
            stack2.append(curr)

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        while stack2:
            curr = stack2.pop()
            print(curr.val)


def post_order(root):
    if not root:
        return root
    else:
        post_order(root.left)
        post_order(root.right)
        print(root.val)

post_order(root)
print("\nWithout recursion\n")
post_order_without_recursion(root)