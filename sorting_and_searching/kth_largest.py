import random

class Solution:
    def findKthLargest(self, nums, k):
        
        def partition(pivotindex, start, end):
            nums[start], nums[pivotindex] = nums[pivotindex], nums[start]
            smaller = start
            for bigger in range(start+1, end+1):
                if nums[bigger] < nums[start]:
                    smaller += 1
                    nums[smaller], nums[bigger] = nums[bigger], nums[smaller]
            nums[start], nums[smaller] = nums[smaller], nums[start]
            return smaller
            
        n = len(nums)
        def quickselect(nums, start, end):
            if start == end:
                return nums[n-k]
            pivotindex = random.randint(start, end)
            smaller = partition(pivotindex, start, end)
            if n - k == smaller:
                return nums[n - k]
            elif n - k < smaller:
                return quickselect(nums, start, smaller - 1)
            else:
                return quickselect(nums, smaller + 1, end)
                
        
        return quickselect(nums, 0, len(nums) - 1)
        

s = Solution()
output = s.findKthLargest([4,5,63,2,1,-21], 1)
print(s.findKthLargest([4,5,63,2,1,-21], 5))
print(s.findKthLargest([4,5,63,2,1,-21], 2))
print(s.findKthLargest([4,5,63,2,1,-21], 3))





