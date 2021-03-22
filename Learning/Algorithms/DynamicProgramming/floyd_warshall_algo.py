# problem is to find shortest path between all the pairs of vertices
# dijkstra can do the job but with O(n2*E)
# so we use another approach of DP
def floydWarshall(graph): # O(n3)
    n = len(graph)
    for k in range(n):
        for i in range(n):
            if k == i:
                continue
            for j in range(n):
                if k==j or i==j:
                    continue
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    return graph

INF = 99
graph = [
    [0,2,3,INF,INF],
    [2,0,15,2,INF],
    [3,15,0,INF,13],
    [INF,2,INF,0,9],
    [INF,INF,13,9,0]
]
print(floydWarshall(graph))