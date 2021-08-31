"""
Given : 

n  = # of vertices with ids 0, 1, 2 ..n - 1
connections = [(src, dst, weight/cost)]


size = [1, 1, ...1]
parent = [0, 1, ....n - 1]
comps = n 


# sort the connections list based on their weight

Code is similar to Union Find (For Union we could use weighted union , 
for find you could use path compression to make it O(1))

Time Complexity:

Sorting in Kruskals:
 ~ O(mlogm)
If graph is dense m ~ n**2

 O(mlog(n**2)) which is O(2mlogn) ~ O(mlogn)

If graph is sparse m = 2n

O(nlogn)

Weighted Union and Find with Path Compression :
O(n)

Total O(n) + O(nlogn) or O(mlogn)  == O(nlogn) or O(mlogn) depending on dense or sparse

"""

def find(x):
	#base case
	if x == parent[x]:
		return x

	#Recursive case
	rootx = find(parent[x])
	parent[x] = rootx
	return rootx

def minSpanningTree(connections, n):
	comps = n 
	totalcost = 0 
	result = []
	for u, v, cost in connections:
		rootu = find(rootu)
		rootv = find(rootv)

		if rootu != rootv:
			if size[rootu] < size[rootv]:
				parent[rootu] = rootv
				size[rootv] += size[rootu]
			else:
				parent[rootv] = rootu
				size[rootu] += size[rootv]

			comps -=1
			totalcost +=cost 
			res.append((u,v))

	if comps == 1 :
		return totalcost #or result of list of edges making the min spanning tree depending on Q
	else:
		return -1


