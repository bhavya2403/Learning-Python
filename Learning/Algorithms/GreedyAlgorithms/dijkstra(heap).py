from heapq import heappop, heappush

def dijkstra(V, u, adj_list, weights):
    minDistances = [10**5] * V
    minDistances[u] = 0
    alrChecked = [False] * V
    heap = [(0, u)]

    while heap: # O(Vlog(E))
        __, minIdx = heappop(heap)
        alrChecked[minIdx] = True

        for idx, v in enumerate(adj_list[minIdx]):
            if minDistances[v] > minDistances[minIdx] + weights[minIdx][idx]:
                minDistances[v] = minDistances[minIdx] + weights[minIdx][idx]
                if not alrChecked[v]:
                    heappush(heap, (minDistances[v], v))

    return minDistances

adj_list = {
    0: [1, 2, 3, 4],
    1: [5, 6, 7],
    2: [5, 6],
    3: [7],
    4: [6, 7],
    5: [8, 9],
    6: [8, 9],
    7: [9, 10],
    8: [11],
    9: [11],
    10: [11],
    11: []
}
weights = {
    0: [9, 7, 3, 2],
    1: [4, 2, 1],
    2: [2, 7],
    3: [11],
    4: [11, 8],
    5: [6, 5],
    6: [4, 3],
    7: [5, 6],
    8: [4],
    9: [2],
    10: [5],
    11: []
}
print(dijkstra(12, 0, adj_list, weights))

