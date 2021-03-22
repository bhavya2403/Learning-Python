# A Multistage graph is a directed graph in which the nodes can be divided into a set of
# stages such that all edges are from a stage to next stage only (In other words there is
# no edge between vertices of same stage and from a vertex of current stage to previous stage)

# brute force: find all possible then minimum (worst possible)
# dijkstra: gives shortest paths from start to all nodes which is not required
# right approach : dp (TABULATION)

def shortestDist(adj_list, weights): # O(E)
    N = len(adj_list)
    cost = [1000] * N
    d = [0] * N
    cost[N-1] = 0
    d[N-1] = N
    for i in range(N - 2, -1, -1): # O(V)
        min = 1000
        min_idx = 0
        for j in range(len(adj_list[i])): # O(e)
            if cost[adj_list[i][j]]+weights[i][j] < min:
                cost[i] = cost[adj_list[i][j]] + weights[i][j]
                min = cost[i]
                min_idx = j
        d[i] = adj_list[i][min_idx]

    idx = d[0]
    print(0, '-',end=' ')
    while idx < N:
        print(idx, '-', end=' ')
        idx = d[idx]

    return '\n' + str(cost[0])

adj_list = {
    0: [1,2,3,4],
    1: [5,6,7],
    2: [5,6],
    3: [7],
    4: [6,7],
    5: [8,9],
    6: [8,9],
    7: [9,10],
    8: [11],
    9: [11],
    10: [11],
    11: []
}
weights = {
    0: [9,7,3,2],
    1: [4,2,1],
    2: [2,7],
    3: [11],
    4: [11, 8],
    5: [6,5],
    6: [4,3],
    7: [5,6],
    8: [4],
    9: [2],
    10: [5],
    11: []
}

print(shortestDist(adj_list, weights))
