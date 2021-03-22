def minCost(matrix):
    n = len(matrix)
    for i in range(1, n):
        matrix[0][i] += matrix[0][i-1]
        matrix[i][0] += matrix[i-1][0]
    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
    return matrix[i][j]


print(minCost([[1,2,3], [4,8,2], [1,5,3]]))