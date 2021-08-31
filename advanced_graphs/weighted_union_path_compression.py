

parent = [] * n
comp = n
def weighted_quick_union():

	#initialize parent array with each incoming edge as it own parent and depth/size 1
	for i in range(n):
		parent[i] = i
		size[i] = 1

	for u,v in edges:
		rootu = find(u)
		rootv = find(v)

		if rootu != rootv:
			if size(rootu) < size(rootv):
				parent[rootu] = rootv
				size[rootv] += size[rootu]

			else:
				parent[rootv] = parent[rootu]
				size[rootu] += size[rootv]
			comp -= 1

	return comp



#Path compression find 
# Amortized time complexity is O(1)

def find(x):
	#return rootx as before
	#after doing path compression

	#base case
	if x == parent[x]:
		return x

	#Recursive case
	rootx = find(parent[x])
	parent[x] = rootx
	return rootx

#simple find O(n)

def find(x):
	while x != parent[x]:
		x = parent[x]
	return x
