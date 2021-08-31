import math

def searchRange(nums, target):
    if not nums:
        return [-1, -1]
    if len(nums) == 1:
        return [0, 0] if nums[0] == target else [-1, -1]
    
    s = 0
    e = len(nums)

    left = math.inf
    right = -math.inf

    def helper(nums, s, e):
        nonlocal left, right
        m = s + (e-s)//2
        if (s<e):
            if nums[m] >= target:
                if(nums[m] == target):
                    left = min(left, m)
                helper(nums, s, m)
            if nums[m] <= target:
                if(nums[m] == target):
                    right = max(right, m)
                helper(nums, m+1, e)
    helper(nums, s, e)

    if left == math.inf and right == -math.inf:
        return [-1, -1]
    else:
        return [left, right]


print(searchRange([5,5,5,6,7,8,8,9],8))