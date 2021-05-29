"""
[8 10 12 15 16 20 25]
0         3        6


"""

def make_bst(arr):
    return make_bst_helper(arr,0, len(arr)-1)

def make_bst_helper(arr, s,e ):
    if not arr or len(arr)==0:
        return

    if(s>e):
        return
    mid = s + (e-s) // 2
    root = TreeNode(arr[mid])
    root.left_ptr = make_bst_helper(arr, s, mid-1)
    root.right_ptr = make_bst_helper(arr, mid+1,e)

    return root


class TreeNode:
    def __init__(self, val):
        self.left_ptr = None
        self.right_ptr = None
        self.val = val


root = make_bst([8,10,12,15,16,20,25])

print(root.val)
print(root.left_ptr.val)
print(root.right_ptr.val)
print(root.left_ptr.left_ptr.val)
print(root.left_ptr.right_ptr.val)
