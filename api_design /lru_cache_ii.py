# lru cache
import defaultdict
class Node:
	def __init__(self, k, v, prev, next):
		self.k = k
		self.v = v
		self.prev = prev
		self.next = next

class LRUCache:
	def __init__(self, capacity):
		self.hmap = {}
		head = None
		tail = None
		self.capacity = capacity

	def get(k):
		if k not in hmap:
			return -1
		move_to_begin(k)
		return head.v


    def put(k, v):
		#case 1 key exists in hmap
		if k is in hmap:
			hmap[k].v = v #hmap[k] is a node in dll
			move_to_begin(k)
			return

		#case 2 #insertion of a new node
		if currsize == capacity:
			del hmap[tail.k]
			penultimate = tail.prev 
			if penultimate is not None: #for single node case
				penultimate.next = None
			tail = penultimate
			currsize -= 1 

		if head is None:
			head = tail = Node(k, v)
		else:
			newnode = Node(k, v)
			newnode.next = head
			head.prev = newnode
			head = newnode

		hmap[k] = head
		currsize += 1

    def move_to_begin(k):
    	node = hmap[k]
    	"""
    	[]<----[]--->[]
    	prev   nde   next 
    	"""

    	if head == node:
    		return

    	prevnode = node.prev
    	nextnode = node.next

    	prevnode.next = nextnode
    	if nextnode is not None:
    		nextnode.prev = prevnode
    	else: #node is tail
    	    tail = prevnode

    	node.next = head, node.prev = None
    	head.prev = node
    	head  = node




