def floydWarshall(graph): # O(n3)
    MAX = max(max(i) for i in graph)
    raisedTo10 = 1
    while True:
        if 10 ** raisedTo10 > MAX:
            MAX = 10 ** raisedTo10
            break
        raisedTo10 += 1

    n = len(graph)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                graph[i][j] = MAX

    for k in range(n):
        for i in range(n):
            if k == i:
                continue
            for j in range(n):
                if k==j or i==j:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(n):
        for j in range(n):
            if graph[i][j] == MAX:
                graph[i][j] = -1
    return graph

n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

mat = floydWarshall(graph)

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=' ')
    print()
