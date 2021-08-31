# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
          
        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next
            
            #reverse group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            new_temp = group_prev.next
            group_prev.next = kth
            group_prev = new_temp
            
        return dummy.next
            
            
    def getKth(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr