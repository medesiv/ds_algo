



def countUnivalSubtrees(root: TreeNode) -> int:
    count = [0]
    
    if root is None:
        return count[0]
    
    def is_unival(node):
        
        if node is None:
            return 
        
        lval = is_unival(node.left)
        rval = is_unival(node.right)
        
        if lval==False or rval==False:
            return False
        if node.left and node.left.val!=node.val:
            return False
        if node.right and node.right.val!=node.val:
            return False
        
        count[0]+=1
        
    is_unival(root)
    return count[0]