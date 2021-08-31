class Solution:
   def upsideDownBinaryTreeDFS(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        globalroot = [None]
        def dfs(node, parent, rightsibling):
            oldleft = node.left
            oldright = node.right
            node.right = parent
            node.left = rightsibling
            
            if oldleft is None and oldright is None:
                globalroot[0] = node
                
            if oldleft:
                dfs(oldleft, node, oldright)
                
        dfs(root, None, None)
        return globalroot[0]

    def upsideDownBinaryTreeBFS(self,root):
        if root is None:
            return None
        q = collections.deque([(root,None,None)])
        while len(q)!=0:
            (node,parent,rightsibling)= q.popleft()
            oldleft=node.left
            oldright = node.right
            node.right = parent
            node.left = rightsibling
            if oldleft is not None:
                q.append((oldleft,node,oldright))
        return node