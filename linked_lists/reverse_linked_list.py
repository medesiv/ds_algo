#https://leetcode.com/problems/reverse-linked-list/submissions/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
           next_temp = curr.next
           curr.next = prev
           prev = curr
           curr = next_temp

        return prev

    def print(self,head: ListNode):
        while head.next is not None:
            print(head.val)
            head = head.next
        print(head.val)


ln = ListNode(1)
ln.next = ListNode(2)
ln.next.next = ListNode(3)
ln.next.next.next = ListNode(4)
ln.next.next.next.next = ListNode(5)

s = Solution()
rev_list = s.reverseList(ln)
s.print(rev_list)



