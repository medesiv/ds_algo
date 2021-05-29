"""
implement heap sort
 [10,6,8,9,7,5,3,8,9]

"""

import heapq

def heap_sort(arr):
    heap = []
    for el in arr:
        heapq.heappush(heap,el)
    ordered = []

    while heap:
        ordered.append(heapq.heappop(heap))

    return ordered


arr = [10,6,8,9,7,5,3,8,9]

print(heap_sort(arr))