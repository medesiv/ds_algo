"""
Graph is bipartite if it has no odd cycles
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        parent = [-1]*n
        visited = [-1]*n
        
        def dfs(s):
            visited[s]=1
            if parent[s]==-1:
                color[s]=1
            else:
                color[s] = 1 - color[parent[s]]
            for neb in graph[s]:
                if visited[neb]==-1:
                    parent[neb]=s
                    if dfs(neb)==False:
                        return False
                else:
                    if color[neb]==color[s]:
                        return False
                    
        for v in range(n):
            if visited[v]==-1:
                if dfs(v) == False:
                    return False
        return True


class Solution:
    def isBipartite(self, graph):

        def bfs(src):
            q = []
            q.push()
            visited[src] = 1
            distance[suorce] = 0
            while len(q) > 0:
                node = q.pop(0)
                for neb in graph[node]:
                    if visited[neb] == -1:
                        visited[neb] = 1
                        parent[neb] = node
                        distance[neb] = 1 + distance[node]
                        q.push(neb)
                    else:
                        if neb != parent[node]:
                            if distance[neb] == distance[node]: #odd length cycle detected
                                return False #not bipartite
                            return True
        return False

        for v in range(n):
            if visited[v] == -1:
                if not bfs(v):
                    return False
        return True




class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [-1]*len(graph)
        color = [-1]*len(graph)
        parent = [-1]*len(graph)
        def bfs(src):
            q = []
            q.append(src)
            visited[src]=1
            color[src]=0
            while len(q)>0:
                n = q.pop(0)
                for neb in graph[n]:
                    if visited[neb]==-1:
                        visited[neb]=1
                        parent[neb]=n
                        q.append(neb)
                        color[neb]=1-color[n]       
                    else:
                        if parent[n]!=neb:
                            if color[neb]==color[n]:
                                return False
            return True
        
        for v in range(0,len(graph)):
            if visited[v]==-1:
                if not bfs(v):
                    return False
        return True



# Instead of three arrays you can take two arrays

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #status -1 : unvisited 0:black 1:white
        status = [-1]*len(graph)
        parent = [-1]*len(graph)
        #outer loop needed for disconnected graphs
        def bfs(v):
            q = []
            q.append(v)
            status[v]=0
            while len(q)>0:
                n = q.pop(0)
                for neb in graph[n]:
                    if status[neb]==-1:
                        status[neb]=1-status[n]
                        parent[neb]=n
                        q.append(neb)           
                    else:
                        if parent[n]!=neb:
                            if status[neb]==status[n]:
                                return False
            return True 
    
        for v in range(0,len(graph)):
            if status[v]==-1:
                if not bfs(v):
                    return False
        return True
    