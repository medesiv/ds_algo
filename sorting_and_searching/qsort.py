"""
implement qsort
 [10,7,5,3,8,9]

 10 7 5 3 8 9


"""
import random

def qsort(arr):
    return helper(arr,0,len(arr)-1)

def helper(arr,s,e):
    #if len is <2 or if s>=e to check arr size is 0 or 1
    if s>=e:
        return
    #select a random number as pivot
    p_indx = random.randint(s,e)

    #swap pivot with first element
    arr[s], arr[p_indx] = arr[p_indx], arr[s]

    orange = s #orange is lesser #green is bigger
    for green in range(s+1,e+1):
        if arr[green] <arr[s]:
            orange+=1
            arr[orange],arr[green]=arr[green],arr[orange]
    #swap back pivot with orange which would be right place for pivot
    arr[s],arr[orange]=arr[orange],arr[s]

    #quick sort based on final index of partition
    helper(arr,s,orange-1)
    helper(arr,orange+1,e)
    return arr



print(qsort([10,7,5,3,8,9]))