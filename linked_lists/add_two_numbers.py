# Definition for singly-linked list.
# https://leetcode.com/problems/add-two-numbers/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        4 3 9   9->3->4
        4 6 8   8->6->4
        9 0 7   7->0>-9
        """
        #sentinel or dummy beginning
        dummy = ListNode(0)
        curr = dummy
        first = l1
        second = l2
        carry = 0

        while first is not None or second is not None:

            x = first.val if first is not None else 0
            y = second.val if second is not None else 0

            sum = carry + x + y
            carry = sum // 10

            curr.next = ListNode(sum % 10)
            curr = curr.next

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            curr.next = ListNode(carry)

        return dummy.next