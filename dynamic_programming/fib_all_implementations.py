#Naive implementation (Exponential O(2^n))
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)

#Top down memoization (O(n))
def fib_memo(n):
    memo = {}
    memo[0], memo[1] = 0,1
    if n in memo:
        return memo[n]

    memo[n] = fib[n-1]+ fib[n-2]
    return memo[n]
#Bottom up linear (O(n) with O(n) space)
def fib(n):
    table = [None]*(n+1)
    table[0],table[1]=0,1
    if n<=2:
        return n
    else:
        for i in range(2,n):
            table[i]=table[i-1]+table[i-2]
        return table[n]

# Bottom up linear (O(n) with O(1) space)
    def fib(n):
        first,second = 1,2
        if n <= 2:
            return n
        else:
            for i in range(2, n+1):
                third = first+second
                first = second
                second = third

            return second


    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        table=[-1]*(n+1)
        table[1], table[2]= 1, 2
        for i in range(3,n+1):
            table[i%3]=table[(i-1)%3]+table[(i-2)%3]
        return table[n%3]