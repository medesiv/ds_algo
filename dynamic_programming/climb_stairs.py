"""
LC 70: https://leetcode.com/problems/climbing-stairs/submissions/
"""


def climbStairs2(self, n: int) -> int:
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second


def climbStairs(self, n: int) -> int:
    if n == 1 or n == 2:
        return n
    table = [None] * (n + 1)
    table[1] = 1
    table[2] = 2
    for i in range(3, n + 1):
        table[i % 3] = table[(i - 1) % 3] + table[(i - 2) % 3]
    return table[n % 3]