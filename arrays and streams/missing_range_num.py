"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Input: nums = [0,1,4,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,3] --> "2->3"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
"""


def ret_missing_ranges(self, nums, lower, upper):
    # formats range in the requested format
    def format_range(lower, upper):
        if lower == upper:
            return str(lower)
        return str(lower) + "->" + str(upper)

    res = []
    lower = lower - 1
    for i in range(len(nums)):
        curr = nums[i]
        # Check if the diff between curr and prev is >=2
        # indicates there is atleast one missing value
        if curr - lower >= 2:
            res.append(format_range(lower + 1, curr - 1))
        lower = curr

    # for the remaining elements left out (if any) after iterating through nums
    if lower + 1 <= upper:
        res.append(format_range(lower + 1, upper))

    return res





