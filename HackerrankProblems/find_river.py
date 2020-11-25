ar = []


def riverSizes(matrix):
    for i in matrix:
        i.insert(0, 0)
        i.append(0)
    matrix.insert(0, [0 for i in range(max(len(i) for i in matrix))])
    matrix.append([0 for i in range(max(len(i) for i in matrix))])
    return riverSize(matrix)


def find_good1s(matrix):
    indX = 1
    while 1 <= indX < len(matrix)-1:
        indY = 1
        while 1 <= indY < len(matrix[indX])-1:
            if matrix[indX][indY] == 1:
                if matrix[indX][indY + 1] == 1 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                    return indX, indY
                if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 1 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                    return indX, indY
                if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 1 and matrix[indX][indY - 1] == 0:
                    return indX, indY
                if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 1:
                    return indX, indY
                if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                    ar.append(1)
                    matrix[indX][indY] = 0
                    return find_good1s(matrix)
            indY += 1
        indX += 1


def solve(matrix, indX, indY, count):
    if 1 <= indX < len(matrix)-1:
        if 1 <= indY < len(matrix[indX])-1:
            if matrix[indX][indY + 1] == 1 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                count += 1
                matrix[indX][indY] = 0
                return solve(matrix, indX, indY + 1, count)
            if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 1 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                count += 1
                matrix[indX][indY] = 0
                return solve(matrix, indX + 1, indY, count)
            if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 1 and matrix[indX][indY - 1] == 0:
                count += 1
                matrix[indX][indY] = 0
                return solve(matrix, indX - 1, indY, count)
            if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 1:
                count += 1
                matrix[indX][indY] = 0
                return solve(matrix, indX, indY-1, count)
            if matrix[indX][indY + 1] == 0 and matrix[indX + 1][indY] == 0 and matrix[indX - 1][indY] == 0 and matrix[indX][indY - 1] == 0:
                matrix[indX][indY] = 0
                count += 1
                ar.append(count)
                return riverSize(matrix)
    else:
        matrix[indX][indY] = 0
        count += 1
        ar.append(count)
        return find_good1s(matrix)


def riverSize(matrix):
    find = find_good1s(matrix)
    if not find:
        return ar
    else:
        count = 0
        indX, indY = find
        return solve(matrix, indX, indY, count)


print(riverSizes([
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]))
