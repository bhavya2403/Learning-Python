def tileStacking(n, m, K):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for j in range(m+1):
        dp[0][j] = 1
    for j in range(1, m+1):
        dp[1][j] = j

    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(min(i,K)+1):
                dp[i][j] += dp[i-k][j-1]

    return dp[n][m]

print(tileStacking(3, 3, 1))
