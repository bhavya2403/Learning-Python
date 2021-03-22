

class Graph:
    def __init__(self, adj_list, weights):
        self.V = len(adj_list)
        self.adj_list = adj_list
        self.weights = weights

    def primMST(self):
        key = [100] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent = [0] * self.V
        parent[0] = -1

        for _ in range(self.V):  # O(V2+E) ~ O(V2) but by heap O(Vlog(V)+E)
            min = 100
            min_idx = 0
            for v in range(self.V):  # O(V) but by forming min heap we can reduce it to O(log(V))
                if key[v] < min and not mstSet[v]:
                    min = key[v]
                    min_idx = v
            mstSet[min_idx] = True

            for idx, v in enumerate(self.adj_list[min_idx]):  # O(e)
                if not mstSet[v] and key[v] > self.weights[min_idx][idx]:
                    key[v] = self.weights[min_idx][idx]
                    parent[v] = min_idx

        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", key[i])


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
g = Graph(adj_list, weights)
g.primMST()  # gives answer for directed graph
