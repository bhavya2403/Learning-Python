def solve(verTaken, adjList, V, path, pos):
    if pos == V:
        if path[0] in adjList[path[V - 1]]:
            print(path)
        return

    for vertex in adjList[path[pos - 1]]:
        if vertex not in verTaken:
            path[pos] = vertex
            verTaken.add(vertex)

            solve(verTaken, adjList, V, path, pos + 1)

            path[pos] = 0
            verTaken.remove(vertex)


def hamiltonianCycle(V, adjList):
    path = [0] * V
    path[0] = 1
    verTaken = {1}
    solve(verTaken, adjList, V, path, 1)


adjList = {
    1: [2, 3, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [1, 2, 4]
}
hamiltonianCycle(5, adjList)
