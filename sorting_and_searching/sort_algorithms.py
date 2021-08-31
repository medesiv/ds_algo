#selection sort

a = [15,2,4,0,9,-1]

def selection_sort(a):

	for i in range(len(a)):
		min_indx = i
		for j in range(i+1,len(a)):
			if(a[j]<a[min_indx]):
				min_indx = j
		a[i],a[min_indx]=a[min_indx],a[i]
	return a

print(selection_sort(a))


#insertion sort

def insertion_sort(a):
	return insertion_sort_helper(a,len(a))

def insertion_sort_helper(a,n):
	if(n<=1):
		return a
	insertion_sort_helper(a, n-2)
	j = n-2
	while j>=1 and a[j]>a[j+1]:
		a[j+1],a[j]=a[j],a[j+1]
		j = j - 1
	return a



print(insertion_sort(a))


def insertion_sort(a):
	for i in range(1, len(a) - 1):
		j = i 
		while j>0 and A[j-1] > A[j]:
			A[j], A[j-1] = A[j-1], A[j]
			j = j - 1