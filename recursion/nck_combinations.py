"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


Hint: This is more of a combinations problem
"""
def nck_combinations(nums,k):
    res = []
    def helper(nums,k,slate,i):

        if len(slate)==k:
            res.append(slate[:])
            return

        if i > len(nums)-1:
            return

        helper(nums,k,slate,i+1)
        slate.append(nums[i])
        helper(nums, k, slate, i + 1)
        slate.pop()

    helper(nums,k,[],0)
    return res

nums = [1,2,3,4]
print(nck_combinations(nums,2))