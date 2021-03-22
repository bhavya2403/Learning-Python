def shortestPath(vertices, start, adj_list):
    dist = [6000]* vertices
    alr_checked = [False]*vertices
    dist[start] = 0
    min = 0
    min_idx = start
    for _ in range(vertices):
        try:
            for idx, v in enumerate(adj_list[min_idx]):
                if dist[v] > min + 6:
                    dist[v] = min + 6
        except:
            pass
        alr_checked[min_idx] = True

        if _==vertices-1:
            break

        min = 6000
        min_idx = 0
        for i in range(vertices):
            if dist[i] < min and not alr_checked[i]:
                min = dist[i]
                min_idx = i

    for d in dist:
        if d==0:
            continue
        if d==6000:
            print(-1, end=' ')
        else:
            print(d, end=' ')
    print()

for _ in range(int(input())):
    vertices, edges = map(int, input().split())
    adj_list = {}
    for _ in range(edges):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if a not in adj_list:
            adj_list[a] = [b]
        else:
            adj_list[a].append(b)

        if b not in adj_list:
            adj_list[b] = [a]
        else:
            adj_list[b].append(a)
    for i in adj_list:
        adj_list[i] = list(set(adj_list[i]))
    start = int(input())-1

    shortestPath(vertices, start, adj_list)