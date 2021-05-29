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


print(fib(7,0,1))
