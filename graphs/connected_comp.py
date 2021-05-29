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

"""
1. Represent the graph in adjacent list / adjacent matrix
2. BFS
3. Driver Code
"""

"""
Time Complexity O(n+m) n = vertices m = edges
"""


"""
psuedo code:

def bfs(src):
    q = []
    visited =[]
    q.push(src)
    visited[src] = 1
    while q:
        n = q.pop(0)
        #for neighbour in adj list
        for neb in adj:
            if visited[neb]==-1:
                visited[neb]=1
                q.push[neb]
            else:

"""