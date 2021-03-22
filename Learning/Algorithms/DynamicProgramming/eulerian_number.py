def eulerianNumber(n,m):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0] = 1

    for i in range(2, n+1):
        for j in range(1, min(n, m+1)):
            dp[i][j] = (i-j)*dp[i-1][j-1] + (j+1)*dp[i-1][j]

    return dp[n][m]

print(eulerianNumber(7, 2))