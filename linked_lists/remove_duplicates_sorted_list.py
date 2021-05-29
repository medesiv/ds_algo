"""
lc #83
"""

import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeDuplicates(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(-math.inf,head)
        pred = sentinel
        curr = head
        while curr is not None:
            if curr.val == pred.val:
                #del curr node
                pred.next = curr.next
            else: #move on
                pred = curr
            curr = curr.next
        head = sentinel.next
        return head
