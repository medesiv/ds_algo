import math
"""
lc 19
"""
class ListNode:
    def __init__(self, val=-math.inf,next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthNodeFromEnd(self,n,head):
        sentinel = ListNode(-math.inf,head)
        leader = sentinel
        i=0
        while i<n:
            leader = leader.next
            i+=1
        follower = sentinel

        pred = None
        while leader is not None:
            leader = leader.next
            pred = follower
            follower = follower.next

        pred.next = follower.next
        head = sentinel.next
        return head


