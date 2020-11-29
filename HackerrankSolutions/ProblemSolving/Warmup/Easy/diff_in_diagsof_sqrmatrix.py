def diag_diff(matrix):
    sum = 0
    sum1 = 0
    indX = 1
    for i in matrix:
        indY = 1
        for j in i:
            if (indX+indY) == len(matrix) + 1:
                sum1 += matrix[indX-1][indY-1]
            if indX == indY:
                sum += matrix[indX-1][indY-1]
            indY += 1
        indX += 1

    if sum1 - sum < 0:
        return sum - sum1
    return sum1-sum


print(diag_diff([[1,2,3],[4,5,6], [7,8,9]]))