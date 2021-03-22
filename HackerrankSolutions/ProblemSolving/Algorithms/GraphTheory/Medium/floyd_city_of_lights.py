def floyd(vertices, adj_matrix):
    for k in range(vertices):
        for i in range(vertices):
            if i==k:
                continue
            for j in range(vertices):
                if j==k or i==j:
                    continue
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k]+adj_matrix[k][j])


vertices, edges = map(int, input().split())
adj_matrix = [[100000 for _ in range(vertices)] for _ in range(vertices)]
for _ in range(edges):
    i, j, we = map(int, input().split())
    i -= 1
    j -= 1
    adj_matrix[i][j] = we
for i in range(vertices):
    adj_matrix[i][i] = 0
floyd(vertices, adj_matrix)


queries = int(input())
for _ in range(queries):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    if adj_matrix[i][j]==100000:
        print(-1)
    else:
        print(adj_matrix[i][j])
