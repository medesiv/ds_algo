
# Union Find in terms of parents 

def union():
	components = n

	for u,v in edges:
		rootu = find(u)
		rootv = find(v)

		if rootu!=rootv:
			parent[rootv] = rootu
			components -=1
		print(components)


def find(x):
	while x != parent[x]:
		x = parent[x]
	return x


#Union find template
components_id = []
comps = n

for u,v in edges:
	leader_u = find(u)
	leader_v = find(v)
	if leader_u!=leader_v:
		component_id[leader_v]=components_id[leader_u]
		comps-=1


def find(x):
	#finds leader of arbitrary vertex x
	curr = x
	while curr != components_id[curr]:
		curr = components_id[curr]
	return curr




