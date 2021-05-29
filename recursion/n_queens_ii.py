"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
Input: n = 4
Output: 2

Input: n = 1
Output: 1

Constraints:

1 <= n <= 9

Ex:
when n = 4
We're converting the 4x4 dimensional array to a single dimension
ex: slate [2,0,_,_] represnts row 0 and row 1 have added queens at col 2 and col 0
"""

def distinct_n_queens(n):
    result = []

    def is_valid(slate,row,col):
        for qrow in range(row):
            qcol = slate[qrow]
            if qcol == col:
                return False
            row_diff = abs(row - qrow)
            col_diff = abs(col - qcol)
            if row_diff == col_diff:
                return False
        return True

    def create_slate(slate,n):
        for i,j in enumerate(slate):
            temp = ['.'] * n
            temp[j]='Q'
            temp_str = ''.join(temp)
            slate[i]=temp_str
        return slate

    def helper(n, row, slate):
        if row == n:
            result.append(create_slate(slate[:],n))
        for col in range(n):
            if(is_valid(slate,row,col)):
                slate.append(col)
                helper(n,row+1,slate)
                slate.pop()

    helper(n,0,[])
    return result

print(distinct_n_queens(4))