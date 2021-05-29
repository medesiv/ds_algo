from node import Node
root = Node(20)
root.left = Node(10)
root.right = Node(22)
root.left.left = Node(0)
root.left.right = None
root.left.left.left = None
root.left.left.right = Node(2)
root.left.left.right.left = Node(1)
root.left.left.right.right = Node(4)


# """
#
#             20
#     10               22
# 0
#     2
#   1   4
# """
#
# """
# Time is O(n)
# Space is O(n)
# """
# def k_smallest_number(root,k):
#     arr=[]
#
#     def helper(root):
#         if not root:
#             return
#         helper(root.left)
#         arr.append(root.val)
#         helper(root.right)
#
#     helper(root)
#     return(arr[k-1])
#
#
# print(k_smallest_number(root,3))


"""
Time is O(h+k)
"""

def k_smallest_number3(root,k):
    count=[0]
    res = [None]
    def dfs(node,k):
        if node is None:
            return None
        if node.left is not None:
            dfs(node.left)
        count[0]+=1
        if(count[0]==k):
            res[0]= node.val
            return
        dfs(node.right,k)

    dfs(root,k)
    return res[0]



def k_smallest_number2(root, k):
    num = k
    def helper2(root):
        nonlocal num # use nonlocal or use mutable objects as shown in below function
        if not root:
            return 0
        left = helper2(root.left)
        if left:
            return left
        num -= 1
        if num == 0:
            return root.val

        right = helper2(root.right)
        return right

    res = helper2(root)
    return res

def k_smallest_number3(root, k):
    num = {'val':k} # use mutable objects incase you want to modify immutable numbers in nested functions
    def helper3(root):
        if not root:
            return 0
        left = helper3(root.left)
        if left:
            return left
        num['val'] -= 1
        if num['val'] == 0:
            return root.val

        right = helper3(root.right)
        return right
    res = helper3(root)
    return res


def kthSmallestWithStack(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right


print(k_smallest_number2(root,3))
#print(kthSmallestWithStack(root,3))