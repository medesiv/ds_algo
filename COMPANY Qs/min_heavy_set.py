"""

3,7,5,6,2

"""



def min_heavy_set(arr):
    arr.sort(reverse=True)
    sum_a=0
    sub_a=[]
    sum_b=sum(arr)
    for i in range(len(arr)):
        sub_a.append(arr[i])
        sum_a+=arr[i]
        sum_b = sum_b - arr[i]
        if(sum_a>sum_b):
            break
    return sorted(sub_a)

arr = [3,7,5,6,2,1]
print(min_heavy_set(arr))








