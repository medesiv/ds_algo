"""
Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1


"""

from collections import defaultdict
class Solution:
    
    def __init__(self):
        self.mp = defaultdict(list)
        self.visited = set()
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = 0
        for e in edges:
            self.mp[e[0]].append(e[1])
            self.mp[e[1]].append(e[0])
            
        for v in range(n):
            if v not in self.visited:
                self.bfs(v)
                comp+=1
                
        return comp
        
        
    def bfs(self,v):
        q = []
        q.append(v)
        self.visited.add(v)
        while len(q)>0:
            node = q.pop(0)
            for neb in self.mp[node]:
                if neb not in self.visited:
                    self.visited.add(neb)
                    q.append(neb)
            