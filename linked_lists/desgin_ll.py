"""
Design linked list lc #707
            []
[] --> []
"""
import math

class ListNode:
    def __init__(self, val=-math.inf,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        
    def get(self,index):
        curr = head, node_index =0
        while curr is not None and node_index!=index:
            curr = curr.next
            node_index+=1

    def addAtHead(self,val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def addAtTail(self,val):
        node = ListNode(val)
        self.tail.next = node
        self.tail=node
        if self.head is None:
            self.head = node
            self.tail = node

    def addAtIndex(self,index,val):

        sentinel = ListNode(-math.inf,self.head)
        pred = sentinel
        curr = head, node_index=0

        while curr is not None and node_index!=index:
            pred = curr
            curr = curr.next
            node_index+=1
        #only for leetcode 707 constraint
        if node_index == index:
            node = ListNode(val, curr)
            pred.next=node

        #when appending item at end of the list
        if node_index == index:
            tail = node

        head = sentinel.next

    def deleteAtIndex(self,index):
        sentinel = ListNode(-math.inf,self.head)
        pred = sentinel
        curr = head, node_index = 0
        while curr is not None and node_index!=index:
            pred = curr
            curr = curr.next
            node_index+=1

        if curr is not None:
            pred.next = curr.next
            if self.tail == curr:
                self.tail = pred
            if self.tail == sentinel:
                self.tail = None

        head = sentinel.next



