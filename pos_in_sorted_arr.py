"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""


def search_range(nums,target):
    result = []
    def left_most(nums,target):
        l_index = -1
        s = 0
        e = len(nums)-1

        while s<=e:
            m = s + (e - s) // 2
            if(nums[m]>=target):
                e = m-1
            else:
                s = m +1
            if(nums[m]==target):
                l_index = m
        return l_index

    def right_most(nums,target):
        r_index = -1
        s = 0
        e = len(nums)-1

        while s<=e:
            m = s + (e - s) // 2
            if (nums[m] <= target):
                s = m+1
            else:
                e = m -1
            if (nums[m] == target):
                r_index = m
        return r_index

    result.append(left_most(nums,target))
    result.append(right_most(nums,target))
    return result

def search_range2(nums,target):
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(nums,target,left):
        lo = 0
        hi = len(nums)

        while lo<hi:
            mid = (lo + hi)//2
            if nums[mid]>target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1
        return lo

    left_idx = extreme_insertion_index(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, extreme_insertion_index(nums, target, False) - 1]

print(search_range([5,7,7,8,8,10],8))