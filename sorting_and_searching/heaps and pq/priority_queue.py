import heapq

                        # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task

class PQ:
    def __init__(self):
        self.count = 0 
        self.pq = []

    def get_count(self):
        self.count+=1
        return self.count

    def add_task(self, task, priority=0):
        if task in entry_finder:
            self.remove_task(task)
        count = self.get_count()
        entry = [priority, count, task]
        #print(entry)
        entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        pass

    def remove_task(self, task):
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop_task(self):
        while pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')





pq = PQ()

pq.add_task(4, 3)
pq.add_task(1, 3)
pq.add_task(8, 2)
pq.add_task(7, 1)

#print(entry_finder)



print(pq.pop_task())
print(pq.pop_task())
print(pq.pop_task())
print(pq.pop_task())



