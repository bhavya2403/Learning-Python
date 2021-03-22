def find(parent, i):
    if parent[i] < 0:
        return i
    return find(parent, parent[i])

def union(parent, i, j):
    if parent[i] > parent[j]:
        parent[j] += parent[i]
        parent[i] = j
    else:
        parent[i] += parent[j]
        parent[j] = i

def minCost(adj_matrix):
    swd = []
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j]:
                swd.append((i, j, adj_matrix[i][j]))
    swd.sort(key=lambda a: a[2])
    tot = 0
    parent = [-1] * n
    count = 0
    for i, j, w in swd:

        ps = find(parent, i)
        if parent[i] >= 0:
            parent[i] = ps
        pd = find(parent, j)
        if parent[j] >= 0:
            parent[j] = pd

        if ps != pd:
            tot += adj_matrix[i][j]

            union(parent, ps, pd)

        if count == n-1:
            break
    return tot

adj_matrix = [[0, 1, 2, 3, 4],
         [1, 0, 5, 0, 7],
         [2, 5, 0, 6, 0],
         [3, 0, 6, 0, 0],
         [4, 7, 0, 0, 0]]
print(minCost(adj_matrix))