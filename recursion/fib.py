#fibonacci



def fib(n):
	if(n<2):	
		return(n)
	else:
		k = fib(n-1) + fib(n-2)
		return(k)


def fib(n,b1,b2):
	if(n==0):
		return b1
	else:
		return fib(n-1,b1,b1+b2)

"""
fib(n) with top down memoization
"""

def fib_memo(n):
    memo = {0:0,1:1}
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1)+fib_memo(n-2)
    return memo[n]



def fib_bottom_up(n):
    table = []
    table.append(0)
    table.append(1)
    for i in range(2,n):
        table.append(table[i-1]+table[i-2])
        # If we just need to return the nth fib value
        # we can create array of size 3 and store
        #table[i%3] = table[(i-1)%3] + table[(i-2)%3]
    return table

print(fib_bottom_up(6))
print(fib_memo(8))

print(fib(7,0,1))
