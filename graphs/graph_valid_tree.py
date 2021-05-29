"""
Given n nodes labeled from 0 -> n-1 and a list of undirected edges (each edge is a pair of nodes), write a function
where these edges make up a valid tree

Example:
    Input : n = 5 , edges = [[0,1],[0,2],[0,3],[1,4]]
    Output : True

    Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    Output: false
"""




def check_if_valid_tree(n):
    q = []
    visited = [-1] * n
    parent = [-1] * n
    comp = 0
    def bfs(src):
        q.push(src)
        visited[src] = 1
        while q:
            n = q.pop(0)
            # for neighbour in adj list
            for neb in adj:
                if visited[neb] == -1:
                    parent[neb] = n
                    visited[neb] = 1
                    q.push[neb]
                else:
                    if parent[n] != neb:
                        # cycle present
                        return True
    for v in range(0,n):
        if visited[v] == -1:
            comp+=1
            bfs(v)