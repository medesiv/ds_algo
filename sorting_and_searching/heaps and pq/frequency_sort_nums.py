from collections import Counter
import heapq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequencies = Counter(nums)
        h = []
        for num, frequency in frequencies.items():
            heapq.heappush(h, (frequency, -num))
        
        res = []
        while h:
            frequency, num = heapq.heappop(h)
            num *= -1            
            res.extend([num for _ in range(frequency)])
        
        return res



class Num:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.num > other.num
            
        return self.freq < other.freq

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dict_t = collections.Counter(nums)
        heap, ans = [], []
        for key,freq in dict_t.items():
            heapq.heappush(heap, Num(key,freq))
        while len(heap):
            val = heapq.heappop(heap)
            for i in range(val.freq):
                ans.append(val.num)
        return ans