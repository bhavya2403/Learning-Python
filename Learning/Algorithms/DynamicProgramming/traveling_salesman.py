minCost = 10000
minPath = []

def solve(u, s, adjMatrix, cost, path, dp):
    global minCost, minPath

    if not s:
        if cost + adjMatrix[u][0] < minCost:
            minCost = cost + adjMatrix[u][0]
            minPath = path + [0]
        dp[str(s)] = minCost

    if str(s) not in dp:
        for v in s:
            if adjMatrix[u][v] != -1:
                solve(v, s-{v}, adjMatrix, cost+adjMatrix[u][v], path+[v], dp)
        dp[str(s)] = minCost

    return dp[str(s)]

def travellingSalesman(adjMatrix):
    solve(0, {i for i in range(1, len(adjMatrix))}, adjMatrix, 0, [0], {})
    print(minCost, minPath)

adj_matrix = [
    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 9, 9, 0]
]
print(travellingSalesman(adj_matrix))

