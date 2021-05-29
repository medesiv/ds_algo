def merge_sort(arr):
    def helper(A,start,end):
        if start>=end:
            return
        mid = start+ (end-start)//2
        helper(A,start,mid)
        helper(A,mid+1,end)

        i = start
        j = mid+1
        aux = []

        while i<=mid and j<=end:
            if A[i]<=A[j]:
                aux.append(A[i])
                i+=1
            else:
                aux.append(A[j])
                j+=1

        while i<=mid:
            aux.append(A[i])
            i+=1
        while j<=end:
            aux.append(A[j])
            j+=1
        A[start:end+1]=aux
        return A
    helper(arr,0,len(arr)-1)
    return arr

print(merge_sort([10,-2,3,150,2,0]))