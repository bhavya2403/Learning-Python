def travellingSalesperson(vertices, adj_matrix):  # T(V(V-1)(V+1)/3) = O(V3)
    def solve(k, S):
        if not S:
            return 0
        min = 100000
        for i in S:
            dist = adj_matrix[k][i] + solve(i, S - {i})
            if dist < min:
                min = dist
        return min

    return solve(0, {i for i in range(1, vertices)})

m, n = map(int, input().split())
vertices = m*n
inf = 100000
# cells in the grid are cities gid: m=rows
adj_matrix = [[inf for _ in range(vertices)] for _ in range(vertices)]
for i in range(vertices):
    adj_matrix[i][i] = 0
for i in range(m):
    arr = list(map(int, input().split()))
    for j in range(n-1):
        adj_matrix[n*i+j][n*i+j+1] = arr[j]
for i in range(m-1):
    arr = list(map(int, input().split()))
    for j in range(n):
        adj_matrix[n*i+j][n*(i+1)+j] = arr[j]

print(travellingSalesperson(vertices, adj_matrix))
# 4 3
# 4 5
# 6 7
# 8 9
# 10 11
# 12 13 14
# 15 16 17
# 18 19 20