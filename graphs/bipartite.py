"""
Graph is bipartite if it has no odd cycles

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
                    visited[neb] = 1
                    q.push[neb]
                    dist[neb] = dist[n]+1
                    parent[neb] = n
                else:
                    if parent[n] != neb:
                        # cycle present
                        if dis[neb] == dist[n]
                         return false
            return True


def dfs(node):
    visited[node]=1
    color[node]=0
    for neb in adj:
        if visited[node]==-1:
            color[neb] = 1 - color[node]
        else:
            if color[node]==color[neb]:
                #odd length cycle
            return False
        return True
"""

