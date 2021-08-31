import random


# Kth smallest 
def quickselect(A, k):
	if len(A) == 0 or (k-1 < 0)  or (k-1 >= len(A)):
		print("invalid input")
	else:
		return quickselecthelper(A, k, 0, len(A) - 1)


def partition(start, end, pivotindex, A):
	A[start], A[pivotindex] = A[pivotindex], A[start]
	smaller = start

	for bigger in range(start+1, end + 1):
		if A[bigger] < A[start]:
			smaller += 1
			A[smaller], A[bigger] = A[bigger], A[smaller]

	A[start], A[smaller] = A[smaller], A[start]
	return smaller 

def quickselecthelper(A, k, start, end):
	if start == end: #k element  subarray
		if start != k - 1:
			print("There is some error here")
		else:
			return A[k - 1]

	pivotindex = random.randint(start, end)
	smaller = partition(start, end, pivotindex, A)

	if k - 1 == smaller:
		return A[k - 1]
	elif k - 1 < smaller:
		return quickselecthelper(A, k, start, smaller - 1)
	else:
		return quickselecthelper(A, k, smaller + 1, end)

nums = [4,5,6,2,-2,3,-99]
#print(sorted(nums))
print(quickselect(nums, 5))


# Kth Largest 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def quickselect(nums, start, end):
            if start == end:
                if start != n - k:
                    print("Some err here")
                else:
                    return nums[n - k]
            pivotindex = random.randint(start, end)
            nums[start], nums[pivotindex] = nums[pivotindex], nums[start]
            smaller = start
            for bigger in range(start+1, end+1):
                if nums[bigger] < nums[start]:
                    smaller += 1
                    nums[smaller], nums[bigger] = nums[bigger], nums[smaller]
            nums[start], nums[smaller] = nums[smaller], nums[start]
            
            if n - k == smaller:
                return nums[n - k]
            elif n - k < smaller:
                return quickselect(nums, start, smaller - 1)
            else:
                return quickselect(nums, smaller + 1, end)
                
        
        return quickselect(nums, 0, len(nums) - 1)