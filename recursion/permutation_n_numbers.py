"""
Given a collection of n distinct numbers return all possible permutations

Ex Input: [1,2,3]
Output:

[
[1 2 3]
[1 3 2]
[2 1 3]
..
..
]

                 123

        1        2       3
     2   3     1   3    2  1

1, 2, 3...n
"""

S = [1, 2, 3]


def permute_n_distinct(S):
    helper(S, 0)


def swap(slate, i, k):
    slate[i],slate[k]=slate[k],slate[i]
    return slate


def helper(slate, i):
    if (len(slate)-1 == i):
        print(slate)
    else:
        for k in range(i,len(S)):
            slate = swap(slate, i, k) # the reason we need swap here is we want to chose remaining elements in each case
            helper(slate, i + 1)
            slate = swap(slate, i, k ) #to give the original slate to the next call

permute_n_distinct(S)



def permute_set_based(orig_str, current_str = ''):
    diff = set(orig_str) - set(current_str)
    calls.append(1)
    if len(diff) == 0:
        permutations.append(current_str)
    else:
        for char in diff:
            permute_set_based(orig_str, current_str + char)
    return (calls, permutations)
calls = []
permutations = []
string_to_permute = '123'

permute_set_based(string_to_permute)
print('sorted permutations: ', sorted(permutations))