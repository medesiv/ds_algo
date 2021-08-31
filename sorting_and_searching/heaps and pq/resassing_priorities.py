def reassignedPriorities(priorities):
    ordered_raw_priorities = sorted(set(priorities))
    #print(f'ordered_raw_priorities: {ordered_raw_priorities}')
    priority_dict = {}
    for i, e in enumerate(ordered_raw_priorities, start=1):
        priority_dict[e] = i
    #print(priority_dict)
    return [priority_dict[e] for e in priorities]


print(reassignedPriorities([10, 30, 70, 30, 70, 90]))

import math
from queue import PriorityQueue
def reassignWithPriorityQueue(priorities = [10, 30, 70, 30, 70, 90]):

    pq = PriorityQueue()

    for p in priorities:
        pq.put(p)


    prev = -math.inf
    i = 0
    mp = {}
    while not pq.empty():
        next_task = pq.get()
        #print(next_task)
        if next_task == prev:
            mp[next_task] = i
        else:
            i += 1
            mp[next_task] = i
        prev = next_task


    return [mp[p] for p in priorities]

print(reassignWithPriorityQueue())