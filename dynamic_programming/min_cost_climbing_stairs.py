"""
lc:746

			___
		___|
	___|
___|


f(n) -- min cost for climbing upto step n
min{f(n-1),f(n-2)}+ cost(n)
There are n unique sub problems

"""

def minCostClimbingStairs():
	table = []
	table[0] = cost[0]
	table[1] = cost[1]

	for i in range(2,n+1):
		table[i]=min(table[i-1],table[i-2])+cost[i]
	return table[-1]