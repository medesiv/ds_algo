class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)
        unique = list(count.keys())
        
        def partition(start, end, pivotindex):
            pivot_frequency = count[unique[pivotindex]]
            unique[start], unique[pivotindex] = unique[pivotindex], unique[start]
            
            
            smaller = start
            for i in range(start+1, end + 1):
                if count[unique[i]] < pivot_frequency:
                    smaller += 1
                    unique[smaller], unique[i] = unique[i], unique[smaller]

            unique[start], unique[smaller] = unique[smaller], unique[start]
            return smaller 
        
        def quickselect(start, end, k_smallest):
            if start == end: #k element  subarray
                return

            pivotindex = random.randint(start, end)
            pivotindex = partition(start, end, pivotindex)

            if k_smallest == pivotindex:
                return
            elif k_smallest < pivotindex:
                quickselect(start, pivotindex - 1, k_smallest)
            else:
                quickselect(pivotindex + 1, end, k_smallest)
            
        n = len(unique) 
        
        quickselect(0, n - 1, n - k)
        
        return unique[n - k:]
        