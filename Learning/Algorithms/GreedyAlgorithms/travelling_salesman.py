class Graph:
    def __init__(self, adj_matrix):
        self.V = len(adj_matrix)
        self.adj_matrix = adj_matrix

    def travellingSalesperson(self):  # T(V(V-1)(V+1)/3) = O(V3)
        def solve(k, S):
            if not S:
                return self.adj_matrix[k][0]
            min = 999
            for i in S:
                dist = self.adj_matrix[k][i] + solve(i, S - {i})
                if dist < min:
                    min = dist
            return min

        return solve(0, {i for i in range(1, self.V)})


adj_matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 9, 9, 0]
]
g = Graph(adj_matrix)
print(g.travellingSalesperson())
