"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

"""
import math

def min_len_subarr_with_sum(arr,target):
    min_win_size = math.inf
    curr_sum=0
    i = 0 # i is window start
    if not arr:
        return 0
    for j in range(len(arr)):
        curr_sum +=arr[j] # j is window end
        while(curr_sum >=target):
            min_win_size = min(min_win_size, j - i+1)
            curr_sum-=arr[i]
            i+=1
    return 0 if min_win_size == math.inf else min_win_size

print(min_len_subarr_with_sum([2,3,1,2,4,3],7))