"""
lc # 237
"""
def deleteNode(node):
    node.val = node.next
    node.next = node.next.next