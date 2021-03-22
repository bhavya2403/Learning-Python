from heapq import heappop, heappush

def prims(V, adj_list, weights):
    key = [100] * V
    key[0] = 0
    mstSet = [False] * V
    parent = [0] * V
    parent[0] = -1
    heap = [(0, 0)]
    push, pop = 0, 0

    for _ in range(V):
        weight, minIdx = heappop(heap)
        pop += 1

        for idx, v in enumerate(adj_list[minIdx]):
            if not mstSet[v] and key[v] > weights[minIdx][idx]:
                key[v] = weights[minIdx][idx]
                parent[v] = minIdx
                heappush(heap, (key[v], v))
                push += 1

    print(push, pop)
    for i in range(1, V):
        print(parent[i], '-', i, ', w:', key[i])

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

print(prims(12, adj_list, weights))
