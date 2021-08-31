"""
 [10,7,5,3,8,9]

            10 7 5   3 8 9

    [10,7]      [5]      [38] [9]

[10]   [7] [5]    [3] [8] [9]

[7,10] [1]


[-1,0,5, 7 , 10]  [1,9,17,50]

"""

def merge_sort(arr):
    if(len(arr)<2):
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    return merge(arr,left,right)

def merge(arr,left,right):
    i=0
    j=0
    k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]= left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]= right[j]
        j+=1
        k+=1
    return arr
test_arr= [10,7,5,3,3,8,9,9]
test_arr2= [100,0]
test_arr3 =[1]
print(merge_sort(test_arr))
