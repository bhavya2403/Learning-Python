def assignMiceHoles(N, M, H):
    M.sort()
    H.sort()
    maxTime = 0
    for i in range(N):
        if abs(M[i] - H[i]) > maxTime:
            maxTime = abs(M[i] - H[i])
    return maxTime