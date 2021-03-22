def pathMaxAv(matrix, n):
    for i in range(n):
        for j in range(n):
            if not i and not j:
                continue
            elif not i:
                matrix[0][j] += matrix[0][j-1]
            elif not j:
                matrix[i][0] += matrix[i-1][0]
            else:
                if matrix[i][j-1] > matrix[i-1][j]:
                    matrix[i][j] += matrix[i][j-1]
                else:
                    matrix[i][j] += matrix[i-1][j]

    return matrix[n-1][n-1]/(2*n-1)

Matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(pathMaxAv(Matrix, 3))
