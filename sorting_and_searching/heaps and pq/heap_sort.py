"""
implement heap sort
 [10,6,8,9,7,5,3,8,9]

"""

import heapq

def heap_sort(arr):
    heap = []
    for i in arr:
        heapq.heappush(heap,i)

    res = []

    while heap:
        res.append(heapq.heappop(heap))
    return res

arr = [10,6,8,9,7,5,3,8,9]

print(heap_sort(arr))