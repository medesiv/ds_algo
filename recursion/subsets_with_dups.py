
"""

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


"""
            []
            /  \
          0 [1] 
            /    \
        0 1  [1,2] 02 [1,2]
           /
    0 1 2  [1,2,2]         
"""

def get_distinct_sets2(s):
    sorted_s = sorted(s)
    res =[]

    def helper(nums, slate,start_indx):
        res.append(slate[:])
        for i in range(start_indx,len(nums)):
            #print(start_indx,i,nums[i],nums[i-1])
            #send the duplicate number only once in the include exclude tree
            if(i!=start_indx and nums[i]==nums[i-1]):
                continue
            slate.append(nums[i])
            helper(nums,slate,i+1)
            slate.pop()

    helper(sorted_s,[],0)
    return res

print(get_distinct_sets2([1,2,2]))


# def get_distinct_sets(s):
#     sorted_s = sorted(s)
#     res =[]
#     def helper(input_arr, i, slate):
#         if (len(input_arr) == i):
#             res.append(slate[:])
#             return
#         # count duplicates
#         count = 1
#         j = i + 1
#         while j < len(input_arr) and (input_arr[i] == input_arr[j]):
#             j += 1
#             count += 1

#         # generate count helper
#         for a in range(0, count+1):
#             for b in range(a):
#                 slate.append(input_arr[i])
#             # call helper for 3 options in example : empty, 2, 22
#             helper(input_arr, i + count, slate)
#             for b in range(a):
#                 slate.pop()
#     helper(sorted_s,0,[])
#     return res


# print(get_distinct_sets([1,2,2]))



