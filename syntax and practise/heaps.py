#heaps

import heapq

arr = [(1,'c'), (1,'a'), (1,'b'), (3,'c'), (3,'a'),(2,'m')]



def test_heap(arr):
	pq = []

	print(sorted(arr,key = lambda x:(-x[0],255 - ord(x[1]))))
	#return arr

	# for e in arr:
	# 	heapq.heappush(pq, (-e[0],e[1]))

	# while len(pq) > 0:
	# 	f, v = heapq.heappop(pq)
	# 	print(-f, v)


print(test_heap(arr))
