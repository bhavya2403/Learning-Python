# no. of edges in graph: E, total vertexes: V, no of cycles = n
# total number of spanning trees: EC(V-1) - n

class Graph:
    def __init__(self, adj_list, weights):
        self.V = len(adj_list)
        self.adj_list = adj_list
        self.weights = weights

    def findParent(self, parent, i):
        if parent[i] < 0:
            return i
        return self.findParent(parent, parent[i])

    def unionOfRoots(self, parent, rootX, rootY):
        if parent[rootX] < parent[rootY]:
            parent[rootX] += parent[rootY]
            parent[rootY] = rootX
        else:
            parent[rootY] += parent[rootX]
            parent[rootX] = rootY

    def kruskalMST(self):  # O(E*log(E))
        we_sr_de = []
        for v in adj_list:  # O(E)
            for idx, u in enumerate(adj_list[v]):
                we_sr_de.append([self.weights[v][idx], v, u])
        we_sr_de.sort()  # O(E*log(E))
        print("Edge \tWeight")
        parent = [-1] * self.V
        count = 0
        for weight, source, destination in we_sr_de:  # O(E)

            parentS = self.findParent(parent, source)  # O(1)
            if parent[source] >= 0:
                parent[source] = parentS  # collapsing unions
            parentD = self.findParent(parent, destination)  # O(1)
            if parent[destination] >= 0:
                parent[destination] = parentD  # collapsing unions

            if parentS != parentD:
                print(source, '-', destination, '\t', weight)
                self.unionOfRoots(parent, parentS, parentD)  # O(1)
                count += 1

            if count == self.V - 1:
                break


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
#     0: [1,2,3],
#     1: [3],
#     2: [3],
#     3: []
# }
# weights = {
#     0: [10,6,5],
#     1: [15],
#     2: [4]
# }
#

g = Graph(adj_list, weights)
g.kruskalMST()  # gives answer for directed graph
