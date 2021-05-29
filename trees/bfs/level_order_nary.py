

class Node:
    def __init(self,val,children):
        self.val = val
        self.children = children

def level_order_nary2(root):
    """
    Using extend instead of append for cleaner code
    """
    if root is None:
        return []
    res = []
    q = []
    q.append(root)
    while len(q) > 0:
        temp = []
        for _ in range(len(q)):
            node = q.pop(0)
            q.extend(node.children)
            temp.append(node.val)
        res.append(temp)
    return res

def level_order_nary(root):
        if root is None:
            return []
        res = []
        q = []
        q.append(root)
        while len(q) > 0:
            num_nodes = len(q)
            temp = []
            for _ in range(num_nodes):
                node = q.pop(0)
                for child in node.children:
                    q.append(child)
                temp.append(node.val)
            res.append(temp)
        return res




