class Graph:
    def __init__(self, adj_list, weights):
        self.V = len(adj_list)
        self.adj_list = adj_list
        self.weights = weights

    def dijkstraShortestPath(self, start):  # T(V2 + E + V) = O(V2)
        shortest_paths = [1000] * self.V
        alr_checked = [False] * self.V
        vertices = {}
        vertices_rev = {}
        i = 0
        for v in self.adj_list:  # O(V)
            vertices[v] = i
            vertices_rev[i] = v
            i += 1
        shortest_paths[vertices[start]] = 0
        for _ in range(self.V):  # T(V2 + E) = O(V2)
            min = 1000
            min_idx = 0
            for idx, dist in enumerate(shortest_paths):  # O(V)
                if dist < min and not alr_checked[idx]:
                    min = dist
                    min_idx = idx

            node = vertices_rev[min_idx]
            for idx, v in enumerate(self.adj_list[node]):  # O(e)
                if self.weights[node][idx] + shortest_paths[min_idx] < shortest_paths[vertices[v]]:
                    shortest_paths[vertices[v]] = self.weights[node][idx] + shortest_paths[min_idx]
            alr_checked[min_idx] = True

        return shortest_paths


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
g = Graph(adj_list, weights)
print(g.dijkstraShortestPath(0))
