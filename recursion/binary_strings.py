# print all binary strings of length 3
#[000,001,010..111]


#DFS -- using slate approach if n == 0 we need to print slate the base case
#Here space complexity is O(n) as max. worker threads will be of depth n

def binary(n):
	return bs_helper("",n)

def bs_helper(slate,n):
	if(n==0):
		print(slate)
	else:
		bs_helper(slate+"0",n-1)
		bs_helper(slate+"1",n-1)

#print(binary(5))



#BFS approach here the space complexity will be O(2^n)
def binary_strings(n):
	if(n==1):
		return ["0","1"]
	else:
		prev = binary_strings(n-1)
		result = []
		for s in prev:
			result.append(s+"0")
			result.append(s+"1")
		return result

#print(binary_strings(5))



def binary3(n):
	res = []
	def bs_helper3(slate,n):
		if(n==0):
			print(''.join([str(i) for i in (slate[:])]))
		else:
			slate.append(0)
			bs_helper3(slate,n-1)
			slate.pop()
			slate.append(1)
			bs_helper3(slate,n-1)
			slate.pop()
	bs_helper3([],n)
	return res



print(binary3(5))
