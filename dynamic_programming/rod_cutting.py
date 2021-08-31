"""
https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
"""

def rodcutting(n,lengths,prices):
	#n = length of the original rod
	#lengths and prices are the prices values for rods of lengths 1, 2, 3, 4 .. which could go well beyond the length n

	if n == 0:
		return 0
	if n == 1:
		return prices[0]

	table = [0 for _ in range(n+1)]
	table[0] = 0
	table[1] = prices[0]

	#In general, if a rod has a length i, then we focus on the last piece of it
	#What could the length of the last peice be
	#It no longer has a constant number of choices. It could vary from 1 to i itself
	#Lets treat the case where we don't cut the rod at all to be the default, and see if we can do better
	#So we will vary the length of the last cut piece from 1 to i-1

	for i in range(2, n+1):
		#Need to compute and set value of table[i]
		best = prices[i-1] #prices array is zero indexed
		for cut in range(1,i):
			if prices[cut - 1] + table [i-cut] > best:
				best = prices[cut - 1] + table[i-cut]
			table[i] = best
	return table[n]

print(rodcutting(4, [1, 2, 3, 4, 5, 6, 7, 8], [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]))