def hourglassSum(matrix):
    arr = []
    i = 0
    for elX in matrix:
        j = 0
        for elY in elX:
            if i < len(matrix) - 2 and j < len(matrix) - 2:
                summ = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j+1] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
                arr.append(summ)
                summ = 0
            j += 1
        i += 1

    return max(arr)


print(hourglassSum([[1 ,1 ,1 ,0 ,0, 0],[0 ,1 ,0 ,0 ,0 ,0],[1 ,1 ,1 ,0 ,0 ,0],[0 ,0 ,2 ,4 ,4 ,0],[0 ,0 ,0 ,2 ,0 ,0],[0 ,0 ,1 ,2 ,4, 0]]))