"""
You are given an integer array arr of size n. Group and rearrange them (in-place) into evens and odds in such a way that group of all even integers appears on the left side and group of all odd integers appears on the right side.

Example

Input: [1, 2, 3, 4]

Output: [4, 2, 1, 3]

Order does not matter. Other valid solutions are:

[2, 4, 1, 3]

[2, 4, 3, 1]

[4, 2, 3, 1]


"""

def solve(a):
    i = 0
    j = len(a)-1
    while i < j:
        if a[i] % 2 == 0:
            i += 1
        elif a[j] % 2 != 0:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i+=1
            j-=1

    return a


arr = [4, 9, 5, 2, 9, 5, 7, 10]
arr2 = [1, 90]
arr3 = [4,6,7]
print(solve(arr3))
