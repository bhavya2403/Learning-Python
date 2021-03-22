def goldMine(n, m, mat):
    if n == 1:
        pass
    for j in range(1, m):
        for i in range(n):
            if not i:
                mat[i][j] += max(mat[i][j - 1], mat[i + 1][j - 1])
            elif not n - 1 - i:
                mat[i][j] += max(mat[i - 1][j - 1], mat[i][j - 1])
            else:
                mat[i][j] += max(mat[i - 1][j - 1], mat[i][j - 1], mat[i + 1][j - 1])

    path = []
    maxIdx, maxi = 0, 0
    for i in range(n):
        if mat[i][m - 1] > maxi:
            maxi = mat[i][m - 1]
            maxIdx = i
    path.append((maxIdx, m - 1))
    i = maxIdx
    goldCollected = mat[i][m - 1]
    for j in range(m - 2, -1, -1):
        maxI, maxV = 0, 0
        for k in range(-1, 2):
            try:
                if mat[i - k][j] > maxV:
                    maxV = mat[i - k][j]
                    maxI = i - k
            except:
                pass
        i = maxI
        path.append((i, j))
    path.reverse()
    return path, goldCollected


mat = [
    [1, 3, 3],
    [2, 1, 4],
    [0, 6, 4]
]
print(goldMine(3, 3, mat))
