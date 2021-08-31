"""
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""

def permtations_with_dups(arr):
    res = []
    def helper(arr, i):
        nonlocal res
        if i == len(arr)-1:
            res.append(arr[:])
        used = set()
        for k in range(i,len(arr)):
            if(arr[k] not in used):
                arr[i],arr[k] = arr[k],arr[i]
                helper(arr,i+1)
                arr[i],arr[k] = arr[k],arr[i]
                used.add(arr[k])
    helper(arr,0)
    return res

def permtations_with_dups_alt(arr):
    res = []
    def helper2(arr, i):
        nonlocal res
        if i == len(arr)-1:
            res.append(arr.copy())
        for k in range(i,len(arr)):
            if(k!=i and arr[k]==arr[i]): #instad of using a set
                continue
            arr[i],arr[k] = arr[k],arr[i]
            helper2(arr,i+1)
            arr[i],arr[k] = arr[k],arr[i]
    helper2(arr,0)
    return res


nums = [1,2,3]
nums2 = [1,2,1]
# print(permtations_with_dups(nums2))

print(permtations_with_dups_alt(nums2))

