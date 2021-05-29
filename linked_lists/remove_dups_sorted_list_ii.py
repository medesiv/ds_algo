"""
lc #82
"""

import math

class ListNode:
    def __init__(self, val=-math.inf,next=None):
        self.val = val
        self.next = next

def remove_dups(head):
    sentinel = ListNode(-math.inf,head)
    
    pred = sentinel
    curr = head
    while curr is not None:
        if curr.next is not None and curr.next.val==curr.val:
            #delete all nodes
            p = curr.next
            while p is not None and p.val==curr.val:
                p=p.next
            pred.next = p
            curr = p
        else:
            pred = curr
            curr = curr.next

    head = sentinel.next
    return head
