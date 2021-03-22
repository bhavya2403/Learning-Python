from strassen import Strassen

def checkPos(l, m, n, o):
    if m != n:
        return False
    if l == m == o:
        return 's'
    return 'n'


def native(l, n, m, a, b):
    matrix = [[0 for _ in range(n)] for _ in range(l)]
    for k in range(m):
        for i in range(l):
            for j in range(n):
                matrix[i][j] += a[i][k] * b[k][j]
    return matrix


def matrixMulti(l, m, n, o, a, b):
    res = checkPos(l, m, n, o)
    if res:
        if res == 'n':
            return native(l, n, m, a, b)
        else:
            return Strassen(a, b)


print(matrixMulti(3, 3, 3, 3, [[1, 4, 11], [2, 5, 12], [13, 14, 15]], [[7, 8, 16], [9, 10, 17], [18, 19, 20]]))
