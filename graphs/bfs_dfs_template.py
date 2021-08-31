"""

dfs(src)
bfs(src)

"""

def dfs(src):
    vistied[src]=1
    for neb in adj_list[src]:
        if visited[src]!=-1:
            dfs(neb)


def bfs(src):
    q = []
    q.append(src)
    visited[src] = 1
    while len(q)>0:
        node = q.pop(0)
        for neb in adj_list[node]:
            if visited[neb]==-1:
                visited[neb]=1
                parent[neb]= node
                q.append(neb)
                

#layer by layer 
def bfs(src):
    q = []
    q.append(src)
    visited[src] = 1
    while len(q)>0:
        for i in range(len(q)):  #This is the key part and similar to trees #used in rotten oranges, word_ladder
            node = q.pop(0)
            for neb in adj_list[node]:
                if visited[neb]==-1:
                    visited[neb]=1
                    parent[neb]= node
                    q.append(neb)

#detect cycle

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
                        # cycle present there is a cross edge
                        return True
    for v in range(0,n):
        if visited[v] == -1:
            comp+=1
            bfs(v)


def check_if_valid_tree_dfs(n):
    adj_map ={}
    visited = [-1] * n
    parent = [-1] * n
    comp = 0
    def dfs(node):
        visited[node] = 1
        for neb in adj_map[node]:
            if visited[neb]==-1:
                #return True that there is a cycle
                parent[neb] = node
                if dfs(neb):
                    return True
            else:
                if neb!=parent[node]:
                    return True #There is a back edge
        return False


def dfs_iterative(graph, start_vertex):
    visited = set()
    traversal = []
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            traversal.append(vertex)
            stack.extend(reversed(graph[vertex]))   # add vertex in the same order as visited
    return traversal

test_graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

print(dfs_iterative(test_graph, 'A'))