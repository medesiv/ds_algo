xclass Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root:None}
        # Since p and q will exist in the tree
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left is not None:
                parents[node.left] = node
                stack.append(node.left)
            if node.right is not None:
                parents[node.right] = node
                stack.append(node.right)
        ancestors = set()
        
        ptr1 = p 
        
        while ptr1:
            ancestors.add(ptr1)
            ptr1 = parents[ptr1]
        
        ptr2 = q
        
        while ptr2 not in ancestors:
            ptr2 = parents[ptr2]
        
        return ptr2     
        