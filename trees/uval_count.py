class Node:
    uval_count = 0
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def print_tree(self, root):
        if root:
            print(root.val)
            self.print_tree(root.left)
            self.print_tree(root.right)

    def get_unival_subtrees_count(self, root):
        self.uval_count = 0

        if (root is None):
            return self.uval_count
        self.helper(root)
        return self.uval_count

    def helper(self, node):

        left_uval=right_uval=my_uval=True
        if(node.left is not None):
            left_uval = self.helper(node.left)
            my_uval = (node.val == node.left.val) and left_uval
        if(node.right is not None):
            right_uval = self.helper(node.right)
            my_uval = (node.val == node.right.val) and right_uval
        if(my_uval):  self.uval_count+=1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

root.print_tree(root)
