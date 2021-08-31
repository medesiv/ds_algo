class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        if n == 3:
            return max(nums[0],nums[1],nums[2])
        if n == 4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
        table = [0]* n 
        #we need to somehow break the circle into a line
        #Let's say the houses were numbered 0..n-1
        
        #Case 1: Suppose the first house, 0 , was robbed
        #In that case, house n-1 couldn't be robbed, and house 1 couldn't be robbed
        #We need to consult the best solutions from 2 ..n-2 treating they're in straight line
        table[2]=nums[2]
        table[3]=max(nums[2],nums[3])
        for i in range(4,n-1):
            table[i] = max(nums[i]+table[i-2],table[i-1])
        case1 = nums[0]+table[n-2]
        #Case 2: Suppose first house was not robbed
        # In that case we need to consult solutions 1..n-1 as if they lie along a line
        table[1] = nums[1]
        table[2] = max(nums[1],nums[2])
        for i in range(3,n):
            table[i] = max(nums[i]+table[i-2],table[i-1])
        case2 = table[n-1]
        
        return max(case1,case2)