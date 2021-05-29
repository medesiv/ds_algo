# Given n distinct integers print the subsets


#
# class Subsets:
#
#     def get_distinct_sets(self,s):
#         return self.helper(s,0,[])
#
#     def helper(self,s,i,slate):
#
#         if(len(s)==i):
#             print(slate)
#             return
#         else:
#             slate.append(s[i])
#             self.helper(s, i + 1, slate)
#             slate.pop()
#             self.helper(s,i+1,slate)
#
# x = Subsets()
# print(x.get_distinct_sets([1,2,3]))


def get_distinct_sets2(s):
    sorted_s = sorted(s)
    res =[]

    def helper_with_for_loop(nums, slate,start_indx):
        res.append(slate[:])
        for i in range(start_indx,len(nums)):
            #print(i,start_indx)
            slate.append(nums[i])
            helper_with_for_loop(nums,slate,i+1)
            slate.pop()

    helper_with_for_loop(sorted_s,[],0)
    return res


print(get_distinct_sets2([1,2,3]))