n = # vertices
adj_list = [] * n

for (u, v, cost) in connections:
	adj_list[u].append((v, cost))
	adj_list[v].append((u, cost))

captured = [] * n 
captured[0] = 1

pq = PriorityQueue()

#Insert all neighbours of vertex 0 into pq with priority_val = weight(0, neighbour)

totalcost = 0

while pq is not empty:
	(node, priority) = pq.extractmin()
	if captured[node] == 1:
		then continue
	captured[node] = 1
	totalcost += priority
	for (neighbour, cost) in adj_list[node]:
		if neighbour is not captured:
			pq.insert((neighbour, priority = cost))

return totalcost


