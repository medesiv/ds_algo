"""
lc # 203
"""
import math
class ListNode:
    def __init__(self, val=-math.inf,next=None):
        self.val = val
        self.next = next

def remove_all_val(head, val):
    sentinel = ListNode(-math.inf,head)
    pred = sentinel
    curr = head
    while curr is not None:
        if curr.val == val:
            #del curr node
            pred.next = curr.next
        else: #move on
            pred = curr
        curr = curr.next
    head = sentinel.next
    return head
