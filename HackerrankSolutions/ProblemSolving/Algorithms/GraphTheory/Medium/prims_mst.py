def prims(tot_ver, tot_edges, adj_list, weights, start):
    alr_checked = [False]*tot_ver
    dist = [100000]*tot_ver
    dist[start-1] = 0
    parent = [0]*tot_ver
    for _ in range(tot_ver-1): # O(V2 + E)
        min = 100000
        min_idx = 0
        for i in range(tot_ver): # O(V)
            if dist[i] < min and not alr_checked[i]:
                min = dist[i]
                min_idx = i

        for idx, v in enumerate(adj_list[min_idx+1]): # O(e)
            if dist[v-1] > weights[min_idx+1][idx] and not alr_checked[v-1]:
                dist[v-1] = weights[min_idx+1][idx]
                parent[v-1] = min_idx+1
        alr_checked[min_idx] = True

    tot_weight = 0
    for i in range(tot_ver): # O(V)
        if parent[i]==0:
            continue
        tot_weight += weights[i+1][adj_list[i+1].index(parent[i])]
    return tot_weight



n, tot_edges = map(int, input().split())
adj_list = {}
weights = {}
for _ in range(tot_edges):
    a, b, weight = map(int, input().split())
    if a not in adj_list:
        adj_list[a] = [b]
        weights[a] = [weight]
    else:
        if b in adj_list[a]:
            weights[a][adj_list[a].index(b)] = weight
        else:
            adj_list[a].append(b)
            weights[a].append(weight)

    if b not in adj_list:
        adj_list[b] = [a]
        weights[b] = [weight]
    else:
        if a in adj_list[b]:
            weights[b][adj_list[b].index(a)] = weight
        else:
            adj_list[b].append(a)
            weights[b].append(weight)
s = int(input())
print(prims(n, tot_edges, adj_list, weights, s))