class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        arr_pre = []
        arr_in = []

        def pre_order(root):
            if root is None:
                arr_pre.append(None)
            else:
                arr_pre.append(root.val)
                pre_order(root.left)
                pre_order(root.right)

        pre_order(root)

        def in_order(root):
            if root is None:
                arr_in.append(None)
            else:
                in_order(root.left)
                arr_in.append(root.val)
                in_order(root.right)

        in_order(root)

        return arr_pre,arr_in

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

    def rserialize(self, root, string):
        """ a recursive helper function for the serialize() function."""
        # check base case
        if root is None:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = self.rserialize(root.left, string)
            string = self.rserialize(root.right, string)
        return string

nn = TreeNode(1)
nn.left = TreeNode(2)
nn.right = TreeNode(3)
nn.right.left = TreeNode(4)
nn.right.right = TreeNode(5)

ser  = Codec()
print(ser.serialize(nn))

print(ser.rserialize(nn,""))