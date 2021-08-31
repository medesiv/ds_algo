import random

def quickselect(A, k):
	if len(A) == 0 or (k-1 < 0)  or (k-1 >= len(A)):
		print("invalid input")
	else:
		return quickselecthelper(A, k, 0, len(A) - 1)

def quickselecthelper(A, k, start, end):
	if start == end: #k element  subarray
		if start != k - 1:
			print("There is some error here")
		else:
			return A[k - 1]

	pivotindex = random.randint(start, end)
	A[start], A[pivotindex] = A[pivotindex], A[start]
	pivot = A[start]
	smaller = start
	biggger = start

	for bigger in range(start+1, end + 1):
		if A[bigger] < A[start]:
			smaller += 1
			A[smaller], A[bigger] = A[bigger], A[smaller]

	A[start], A[smaller] = A[smaller], A[start]

	if k - 1 == smaller:
		return A[k - 1]
	elif k - 1 < smaller:
		return quickselecthelper(A, k, start, smaller - 1)
	else:
		return quickselecthelper(A, k, smaller + 1, end)

nums = [4,5,6,2,-2,3,-99]
print(sorted(nums))
print(quickselect(nums, 3))