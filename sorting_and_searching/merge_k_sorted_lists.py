

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O ()
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        def merge(l1, l2):
            res = ListNode(-1)
            curr = res
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    
                curr = curr.next
            if not l1:
                curr.next=l2
            else:
                curr.next=l1
                
            return res.next        
                    
            
        
        def helper(lists, start, end):
            if start == end:
                return lists[start]
            mid = start + (end - start)//2
            
            left = helper(lists, start, mid)
            right = helper(lists, mid+1, end)
            
            return merge(left, right)
        
        
        
        return helper(lists, 0, len(lists) -1)
        




#Alternative approach


class Solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        
        def merge(l1, l2):
            res = ListNode(-1)
            curr = res
            
            while l1 is not None or l2 is not None:
                if l1 == None:
                    curr.next = l2
                    l2 = l2.next
                elif l2 == None:
                    curr.next = l1
                    l1 = l1.next
                elif l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            return res.next        
                    
            
        
        def helper(lists, start, end):
            if start == end:
                return lists[start]
            mid = start + (end - start)//2
            
            left = helper(lists, start, mid)
            right = helper(lists, mid+1, end)
            
            return merge(left, right)
        
        
        
        return helper(lists, 0, len(lists) -1)