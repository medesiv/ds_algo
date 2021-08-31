dfs_with_bookkeeping_template

#dfs with arrival and departure times for bookkeeping
def dfs(node):
	visited[node] = 1
	arrival[node] = timestamp[0]
	timestamp[0] +=1
	for neb in adj_list[node]:
		if visited[neb] == -1:
			if dfs(neb):
				return True
		else:
			if departure[neb] == -1:
				#cycle found
				return True
	departure[node] = timestamp[0]
	timestamp[0] += 1

	

