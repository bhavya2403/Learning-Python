# in the case of negative distance edge graphs dijkstra algorithm is giving wrong answer
# in dijkstra we are already selecting smallest dist edge everytime because we've assumed that
# everytime the distance is going to increase but in this case bcz of negative distance the total
# distance can decrease as well so we've to check dijkstra algorithm V times
# but still there's issue: in case of graph containing a negative weight cycle the weight keeps
# on decreasing everytime i increases so for this case graph cannot be solved

def BFShortestPath(V, start, edges):  # O(VE)
    dist = [10**5] * V
    dist[start] = 0

    for _ in range(V-1):
        relaxed = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                relaxed = True
                dist[v] = dist[u]+w
        if not relaxed:
            break

    for u, v, w in edges:
        if dist[v] > dist[u]+w:
            return "negative weight cycle"

    return dist


# Question: detect a negative weight cycle
# Answer: if we perform above loop one more time if weight is changing then True

# adj_list = {
#     1: [2,3],
#     2: [3,4],
#     3: [5],
#     4: [6],
#     5: [4,6],
#     6: []
# }
# weights = {
#     1:[2,4],
#     2:[1,7],
#     3:[3],
#     4:[1],
#     5:[2,5],
#     6:[]
# }
# adj_list = {
#     1: [2,3,4],
#     2: [3,4],
#     3: [5],
#     4: [1,5],
#     5: [2,3],
#     6: [5]
# }
# weights = {
#     1: [50,45,10],
#     2: [10,15],
#     3: [30],
#     4: [10,15],
#     5: [20,35],
#     6: [3],
# }
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
# adj_list = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [2, 5],
#     4: [3, 6],
#     5: [7],
#     6: [7],
#     7: []
# }
# weights = {
#     1: [6, 5, 5],
#     2: [-1],
#     3: [-2, 1],
#     4: [-2, -1],
#     5: [3],
#     6: [3],
#     7: [],
# }
edges = []
for u in adj_list:
    for idx, v in enumerate(adj_list[u]):
        edges.append((u, v, weights[u][idx]))
print(BFShortestPath(12, 0, edges))
