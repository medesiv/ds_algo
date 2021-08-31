class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # [ai,bi] indicates that you must take course bi first if you want to take course ai.
        ans = []
        indegree = [0]*numCourses
        nebs = defaultdict(list)
        for post, pre in prerequisites:
            indegree[post] += 1
            nebs[pre].append(post)
        
        que = collections.deque([node for node in range(numCourses) if indegree[node]==0])
        while que:
            cur = que.popleft()
            ans.append(cur)
            if nebs[cur]:
                for j in nebs[cur]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        que.append(j)
        if sum(indegree) == 0:
            return ans
        else:
            return []
        
       
        
        