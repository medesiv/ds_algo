"""

arr1 = [1 3 5]

arr2 = [2 4 6 0 0 0]


"""

def merge_two_arrs(arr1,arr2):


    if len(arr2)>len(arr1):
        k = len(arr2) -1
        i = len(arr1) - 1
    else:
        k=len(arr1) -1
        i = len(arr2) - 1

    j=k//2

    while j>=0 and i>=0:
        if arr2[j] >= arr1[i]:
           arr2[k] = arr2[j]
           j-=1
        else:
            arr2[k]=arr1[i]
            i-=1
        k-=1
    while i>=0:
        arr2[k]=arr1[i]
        k-=1
        i-=1
    while j>=0:
        arr2[k] = arr2[j]
        k-=1
        j-=1
    return arr2


print(merge_two_arrs([1,3,5],[2,4,6,0,0,0]))