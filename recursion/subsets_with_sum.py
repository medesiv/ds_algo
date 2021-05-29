"""
arr = [1,2,3,4,5]
K= 5
output: [[2,3], 1,4]]
"""

def get_subsets_with_k_sum(s,target_sum):
    res =[]
    def helper(s, i, slate,target_sum,slate_size, curr_sum):
        if curr_sum>target_sum:
            return
        if curr_sum == target_sum:
            res.append(slate[:])
            return
        if (len(s) == i):
            return
        helper(s,i+1,slate,target_sum,slate_size,curr_sum)
        slate.append(s[i])
        helper(s,i+1,slate,target_sum,slate_size+1,curr_sum+s[i])
        slate.pop()

    helper(s,0,[],target_sum,0,0)
    return res

print(get_subsets_with_k_sum([1,2,3,4,5],5))