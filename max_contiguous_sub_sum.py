"""
Max sum of a contiguous subarray of size 3
arr = [4,2,1,7,8,1,2,8,1,0]
output = 16

"""
import math
"""
Optimal solution O(n) space : O(1)
"""

def max_subarr_sum2(arr,width):
    max_sum = -math.inf
    current_sum=0
    for i in range(len(arr)):
        current_sum +=arr[i]
        if(i>=width-1):
            max_sum = max(max_sum,current_sum)
            current_sum -=arr[i-(width-1)]
    return max_sum

def max_subarr_sum(arr,width):
    max_sum = -math.inf
    sub_arr = []
    i=0
    while i < len(arr):
        while len(sub_arr)<width:
            sub_arr.append(arr[i])
            i+=1
        if sum(sub_arr)>max_sum:
            max_sum = sum(sub_arr)
        sub_arr.pop(0)
    return max_sum


print(max_subarr_sum2([4,2,1,7,8,1,2,8,1,0],3))