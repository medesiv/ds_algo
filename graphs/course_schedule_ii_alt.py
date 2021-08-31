from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #initialize 
        mp, res = {}, []
        for i in range(numCourses):
            mp[i] = Node()
            
        for post, pre in prerequisites:
            mp.get(post).indegree += 1
            mp.get(pre).nebs.append(post)
            
        q = deque()   
        
        for i in range(numCourses):
            if mp.get(i).indegree == 0:
                q.append(i)
                    
        while len(q) > 0:
            node = q.popleft()
            res.append(node)
            for neb in mp.get(node).nebs:
                mp.get(neb).indegree -= 1
                if mp.get(neb).indegree == 0:
                    q.append(neb)
                    
        for node in mp.values():
            if node.indegree != 0:
                return []
            
        return res
        
                    
            
        
        
class Node:
    def __init__(self, nebs = list(), indegree = 0):
        self.indegree = indegree
        self.nebs = list()
        