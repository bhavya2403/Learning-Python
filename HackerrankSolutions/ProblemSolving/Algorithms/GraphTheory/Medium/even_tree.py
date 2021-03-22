def evenTree(adj_list):
    nodes_below = {i:[0 for _ in range(len(adj_list[i]))] for i in adj_list}
    def solve(node):
        if node not in adj_list:
            return 0
        count = 0
        for idx, v in enumerate(adj_list[node]):
            a = 1 + solve(v)
            count += a
            nodes_below[node][idx] = a
        return count

    solve(1)
    count = 0
    for node in nodes_below:
        for v in nodes_below[node]:
            if v % 2 == 0:
                count += 1
    return count

vertices, edges = map(int, input().split())
adj_list = {}
for _ in range(edges):
    b, a = map(int, input().split())
    if a not in adj_list:
        adj_list[a] = [b]
    else:
        adj_list[a].append(b)
print(evenTree(adj_list))
