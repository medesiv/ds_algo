class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj_list = [[] for _ in range(n)]
        for src,dst in prerequisites:
            adj_list[dst].append(src)
        visited = [-1]*n
        timestamp = [0]
        arrival = [-1]*n
        departure = [-1]*n
        
        def dfs(source):
            arrival[source] = timestamp[0]
            timestamp[0]+=1
            visited[source]=1
            for neb in adj_list[source]:
                if visited[neb]==-1:
                    if dfs(neb):
                        return True
                else:
                    if departure[neb]==-1: #cycle is found if dep time is not set for a neb that is visited => backedge
                        return True
            departure[source] = timestamp[0]
            timestamp[0]+=1
        
        for v in range(n):
            if visited[v]==-1:
                if dfs(v):
                    return False
                
        return True
            