
"""
LC: https://leetcode.com/problems/reconstruct-itinerary/

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        itinerary = []
        adj = {}
        for s,d in tickets:
            adj[s]=[]
            adj[d]=[]
            
        tickets.sort(reverse=True)
        
        for s,d in tickets:
            adj[s].append(d)
            
        print(adj["JFK"])
        
        def dfs(s):
            while(len(adj[s])>0):
                neb = adj[s].pop()
                dfs(neb)
            itinerary.append(s)
                
                
        dfs('JFK')
        
        return reversed(itinerary)