"""

Given a series of game results such as xxxx beats yyyy, output the final ranking.

Example 1:

Input: ["a beats b", "b beats c", "c beats d"]
Output: ["a", "b", "c", "d"]
Example 2:

Input: ["a beats b", "a beats c"]
Output: ["a", "b", "c"] or ["a", "c", "b"]
"""
from collections import defaultdict, deque
def final_ranking(arr):
	indegree = {}
	res = []
	adj_list = defaultdict(list)

	def build_graph(arr):
		for r in arr:
			w, l = r.split(" beats ")
			indegree.setdefault(w, 0)
			indegree[l] = indegree.get(l,0) + 1
			adj_list[w].append(l)
		return adj_list

	adj_list = build_graph(arr)

	q = deque([v for v in indegree if indegree[v] == 0])
	while len(q) > 0:
		node = q.popleft()
		res.append(node)
		for neb in adj_list[node]:
			indegree[neb] -= 1
			if indegree[neb] == 0:
				q.append(neb)

	return ''.join(res)

arr = ["a beats b", "b beats c", "c beats d"]
arr1 = ["a beats b", "a beats c"]
inputs = [arr, arr1]

for i in inputs: 
	print(final_ranking(i))




