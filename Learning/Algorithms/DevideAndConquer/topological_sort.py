def solve(u,  visited, stack, adj):
    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            solve(v, visited, stack, adj)

    stack.append(u)


def topoSort(V, adj):
    visited = [False] * V
    stack = []

    for i in range(V):
        if not visited[i]:
            solve(i, visited, stack, adj)

    return stack[::-1]

for _ in range(int(input())):
    e, N = map(int, input().split())
    adj = [[] for _ in range(N)]

    for i in range(e):
        u, v = map(int, input().split())
        adj[u].append(v)

    print(topoSort(N, adj))