from node import Node

root = Node(1)
root.construct_default_tree(root)

def level_order_2queues(root):
    q1 = []
    q2 = []
    lsum=0
    # if root is null we return null
    if root is None:
        return None

    # otherwise push it onto first queue
    q1.append(root)

    # if root has left/right child push them on second queue
    if root.left is not None:
        q2.append(root.left)
    if root.right is not None:
        q2.append(root.right)

    # pop the first queue
    el = q1.pop(0)
    print("\t\t"+str(el.val),"\n")
    while(len(q1)>0 or len(q2)>0):

        if(len(q1)==0):
            while(len(q2)>0):
                q2node = q2.pop(0)
                print("\t"+str(q2node.val),end='\t')
                lsum = lsum + q2node.val
                if q2node.left is not None:
                    q1.append(q2node.left)
                if q2node.right is not None:
                    q1.append(q2node.right)
        print("sum at level is \t",lsum,end="\n")
        #if first q is empty pop from second q if it has children push onto first queue until 2md is empty
        lsum=0
        if(len(q2)==0):
            while(len(q1)>0):
                q1node = q1.pop(0)
                print(" "+str(q1node.val),end='\t')
                lsum = lsum+q1node.val
                if q1node.left is not None:
                    q2.append(q1node.left)
                if q1node.right is not None:
                    q2.append(q1node.right)
        print("sum at level is \t", lsum, end="")
    pass


level_order_2queues(root)