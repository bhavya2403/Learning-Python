import sys
from heapq import heappop, heappush

def dijkstra(V, u, adj_list, weights):
    minDistances = [10**5] * V
    minDistances[u] = 0
    alrChecked = [False] * V
    heap = [(0, u)]

    for _ in range(V): # O(Vlog(E))
        __, minIdx = heappop(heap)
        alrChecked[minIdx] = True

        for idx, v in enumerate(adj_list[minIdx]):
            if minDistances[v] > minDistances[minIdx] + weights[minIdx][idx]:
                minDistances[v] = minDistances[minIdx] + weights[minIdx][idx]
                heappush(heap, (minDistances[v], v))

    for d in minDistances:
        if d==0:
            continue
        if d==10**5:
            print(-1, end=' ')
        else:
            print(d, end=' ')
    print()

i = sys.stdin.readline()
for _ in range(int(i)):
    vertices, edges = map(int, sys.stdin.readline().split())
    adj_list = {}
    weights = {}
    for _ in range(edges):
        a, b, we = map(int, sys.stdin.readline().split())
        a -= 1
        b -= 1
        if a not in adj_list:
            adj_list[a] = [b]
            weights[a] = [we]
        else:
            adj_list[a].append(b)
            weights[a].append(we)

        if b not in adj_list:
            adj_list[b] = [a]
            weights[b] = [we]
        else:
            adj_list[b].append(a)
            weights[b].append(we)
    start = int(input())-1

    dijkstra(vertices, start, adj_list, weights)
