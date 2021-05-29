"""

dfs(node):

    visited[node]=1
    for neb in adj_list[node]:
        if visited[node] == -1:
            dfs(neb)

Time - O (m + n) or O(m) + O(n)
Space - O(m) + O(n)

n = 5
e = [[0,1], [1,2], [3,4]]
0->1
1->0,2
2->1
3->4
4->3

"""