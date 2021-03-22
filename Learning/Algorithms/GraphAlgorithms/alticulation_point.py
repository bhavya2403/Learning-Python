# any graph has a articulation point if by removal of that component breaks the graph in computer
# networks we don't want any articulation point because if one point fails to work then entire network
# will not work, to remove that problem we connect two children of the articulation point

# approach 1: O(V*(V+E))
# for every vertex v:
#   remove v from graph
#   see if graph is still connected (use dfs or bfs)
#   add v back to graph
def articulation(V, adj_list):
    artPoints = []
    for v in adj_list:
        removedVList = adj_list.copy()
        removedVList.__delitem__(v)
        bfs = []
        len_bfs = 0
        queue = [1 if v!=1 else 2]
        visited = [False] * V
        while queue:
            curr = queue.pop()
            if not visited[curr-1] and curr!=v:
                if curr not in bfs:
                    bfs.append(curr)
                    len_bfs += 1
                queue = removedVList[curr] + queue
            visited[curr-1] = True

        if len_bfs != V-1:
            artPoints.append(v)

    return artPoints

# approach 2: O(V+E)
# vertex u is a articulation point if:
# 1> u is not root of DFS tree and it has a child v such that no vertex in subtree rooted with
#    v has a back edge to one of the ancestors (in DFS tree) of u.(means if we take edge 3-5, now
#    if 5's children(6) has a back edge to one of the parents of 3(4,1) which 6 has so 3 is an
#    articulation point because the only way 6 can reach 1 is a back edge going through 3 so on
#    removing 3 that edge gets disconnected)
# 2> u is a root of dfs tree and has more than 1 children

#      1   dfsTree:  (1,1)1     6 has a back edge to 3
#    /   \               /      2 has a back edge to 1
#   4     2        (2,1)4       vertex u:(disc, low)
#    \   /             /
#      3         (3,1)3---2(6,1)
#     / \            /
#    5---6     (4,3)5---6(5,3)

# for case 1 we maintain a disc[]- discovery time for each vertex and earliest visited vertex
# (means by taking path downwards by taking maximum 1 back edge till how low node we can reach)
# so we also maintain low[] and of course for performing dfs we need visited[]
# and parent[], parent[v] = u

def articulationPoint(V, adj_list):
    pass

adj_list = {
    1: [2],
    2: [3,1],
    3: [4,2],
    4: [3]
}
print(articulation(4, adj_list))