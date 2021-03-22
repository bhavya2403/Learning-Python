def seqOfSeq(m, n):
    t = [[0 for _ in range(m+1)] for _ in range(n+1)]
    t[0][0] = 1
    for i in range(1, m+1):
        t[1][i] = i
    for i in range(2, n+1):
        for j in range(1, m+1):
            t[i][j] = t[i-1][j//2] + t[i][j-1]

    return t[n][m]

print(seqOfSeq(5, 2))
