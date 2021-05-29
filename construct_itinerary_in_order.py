"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.

            JFK
        MUC
            LHR
                SFO
                    SJC

    JFK
ATL     SFO


        JFK -> MUC
        MUC-> LHR
        LHR->SFO
        SFO->SJC

        JFK -> ATL, SFO
        ATL -> JFK, SFO
        SFO -> ATL

"""


def findItinerary(self, tickets):
    adj = {}
    res = []
    # print(tickets)
    # tickets.sort(reverse=True)
    # print(tickets)
    for src, dst in tickets:
        adj[src] = []
        adj[dst] = []

    for src, dst in tickets:
        adj[src].append(dst)
        adj[src].sort(reverse=True)

    def dfs(node):

        while (len(adj[node]) > 0):
            neb = adj[node].pop()
            dfs(neb)
        res.append(node)

    dfs('JFK')
    return reversed(res)




"""
Older approach


from collections import defaultdict
def construct_itinerary(s):
    adj_list, visited = {},{}
    for edge in s:
        if edge[0] not in adj_list:
            adj_list[edge[0]]=[edge[1]]
        else:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[0]].sort()

    for k,itinerary in adj_list.items():
        visited[k]=[False]*len(itinerary)

    res = []
    print(visited)
    print(adj_list)
    def dfs(src,route):
        nonlocal res
        if len(route) == len(s)+1:
            res = route
            return True
        for i,next_dest in enumerate(adj_list.get(src,[])): #since we're not using defaultdict we use get
            if not visited[src][i]:
                visited[src][i]=True
                ret = dfs(next_dest,route+[next_dest])
                visited[src][i]=False
                if ret:
                    return True
        return False

    dfs('JFK', ['JFK'])

    return res



s = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
s2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
s3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(construct_itinerary(s3))


"""