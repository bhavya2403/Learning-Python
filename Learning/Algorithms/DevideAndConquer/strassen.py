def removingZeros(n, c):
    l = len(c)
    for _ in range(l-n):
        c.pop()
    for i in range(n):
        c[i] = c[i][:n]

    return c

def addingZeros(l, a, b):
    dim = l
    pow = 0
    while dim >= 1:
        dim = dim / 2
        pow += 1
    dim = 2 ** pow

    for i in range(l):
        a[i] += [0] * (dim - l)
        b[i] += [0] * (dim - l)
    for i in range(dim - l):
        a.append([0] * dim)
        b.append([0] * dim)

    return a, b

def combine(sumMatrices, minusMatrices):
    n = len(sumMatrices[0])
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            plus = sum(matrix[i][j] for matrix in sumMatrices)
            minus = sum(matrix[i][j] for matrix in minusMatrices)
            c[i][j] = plus - minus
    return c


def split(matrix):
    n = len(matrix) // 2
    a, b, c, d = [], [], [], []
    for i in range(n):
        a.append(matrix[i][:n])
        b.append(matrix[i][n:])
        c.append(matrix[i + n][:n])
        d.append(matrix[i + n][n:])

    return a, b, c, d


def strassen(x, y): # T(n)
    if len(x) == 1:
        return x[0][0] * y[0][0]

    a, b, c, d = split(x)
    e, f, g, h = split(y)

    fMinusH = combine([f], [h])
    aPlusB = combine([a, b], [])
    cPlusD = combine([c, d], [])
    gMinusE = combine([g], [e])
    aPlusD, ePlusH = combine([a, d], []), combine([e, h], [])
    bMinusD, gPlusH = combine([b], [d]), combine([g, h], [])
    aMinusC, ePlusF = combine([a], [c]), combine([e, f], [])

    p1 = strassen(a, fMinusH) # T(n/2)
    p2 = strassen(aPlusB, h) # T(n/2)
    p3 = strassen(cPlusD, e) # T(n/2)
    p4 = strassen(d, gMinusE) # T(n/2)
    p5 = strassen(aPlusD, ePlusH) # T(n/2)
    p6 = strassen(bMinusD, gPlusH) # T(n/2)
    p7 = strassen(aMinusC, ePlusF) # T(n/2)

    if type(p1) == list: # O(n^2)
        c11 = combine([p5, p4, p6], [p2])
        c12 = combine([p1, p2], [])
        c21 = combine([p3, p4], [])
        c22 = combine([p1, p5], [p3, p7])

        for i in range(len(c11)):
            c11[i] += c12[i]
        for i in range(len(c11)):
            c21[i] += c22[i]
        c1, c2 = c11, c21
    else:
        c11 = p5 + p4 - p2 + p6
        c12 = p1 + p2
        c21 = p3 + p4
        c22 = p1 + p5 - p3 - p7

        c1 = [[c11, c12]]
        c2 = [[c21, c22]]

    return c1 + c2


def Strassen(a, b):
    n = len(a)
    a, b = addingZeros(n, a, b)
    c =  strassen(a, b)
    return removingZeros(n, c)
