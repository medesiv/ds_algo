import math
import collections
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def height(self,root):

        return self.height_helper(root)

    def height_helper(self,root):

        if root is None:
            return 0

        lheight = self.height_helper(root.left)
        rheight = self.height_helper(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def construct_default_tree(self, root):
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(4)
        root.left.right = Node(3)
        root.right.left = Node(6)
        root.right.right = Node(7)
        # root.right.right.right = Node(8)
        # root.right.right.right.right = Node(9)
        # root.right.right.right.right.right = Node(10)
        # root.right.right.right.right.right.right = Node(11)

    def print_level_tree2(self, root):
        '''
        print level order based on count at each level
        '''
        if root is None:
            return []
        res = []
        q = collections.deque([root])
        while len(q)!=0:
            num_nodes = len(q)
            temp = []
            for _ in range(num_nodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                temp.append(node.val)
            res.append(temp)
        return res

    def print_level_tree(self, root):
        '''
        By pushing infinity whenever there is a new level
        :param root:
        :return:
        '''
        q = []
        # if root is none
        if root is None:
            return
        else:
            q.append(root)
            q.append(math.inf)
            while q:
                t = q.pop(0)
                if t == math.inf and q:
                    q.append(math.inf)
                    print()
                    continue
                if t != math.inf:
                    print("\t",t.val,end='')
                    if t.left:
                        q.append(t.left)
                    if t.right:
                        q.append(t.right)
