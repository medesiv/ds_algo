def postorder_traversal(root):
    stack = []
    stack2 = []
    if not root:
        return root
    else:
        curr = root
        stack.append(curr)
        while stack:
            curr = stack.pop()
            stack2.append(curr)

            if curr.left_ptr:
                stack.append(curr.left_ptr)
            if curr.right_ptr:
                stack.append(curr.right_ptr)

        while stack2:
            curr = stack2.pop()
            print(curr.val)
