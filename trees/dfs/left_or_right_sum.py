class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def solution(arr):
    if len(arr) <= 1:
        return ""
    root = Node(arr[0])
    temp, q = root, []
    q.append(root)
    i = 0
    while len(q) > 0:
        for _ in range(len(q)):
            temp = q.pop(0)
            #print(i)
            if 2*i + 1 < len(arr):
                temp.left = Node(arr[2*i+1])
                q.append(temp.left)
            if 2*i + 2 < len(arr):
                temp.right = Node(arr[2*i+2])
                q.append(temp.right)
            i +=1
            
    res = []
    def dfs(node):
        if node is not None:
            res.append(node.val)
        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
        
    dfs(root.left)
    left_sum = sum(res)
    dfs(root.right)
    right_sum = sum(res) - left_sum
    
    if left_sum > right_sum:
        return "Left"
    elif left_sum < right_sum:
        return "Right"
    else:
        return ""
    
    
    pass
