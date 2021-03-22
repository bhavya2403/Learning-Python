import sys

def dijkstra(vertices, inf, adj_list, weights, start):
    dist = [inf]* vertices
    alr_checked = [False]*vertices
    dist[start] = 0
    min = 0
    min_idx = start
    for _ in range(vertices):
        for idx, v in enumerate(adj_list[min_idx]):
            if dist[v] > min + weights[min_idx][idx]:
                dist[v] = min + weights[min_idx][idx]
        alr_checked[min_idx] = True

        if _==vertices-1:
            break

        min = inf
        min_idx = 0
        for i in range(vertices):
            if dist[i] < min and not alr_checked[i]:
                min = dist[i]
                min_idx = i

    for d in dist:
        if d==0:
            continue
        if d==10e5:
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


    dijkstra(vertices, 10**5, adj_list, weights, start)