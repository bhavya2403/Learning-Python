def noOfWays(m, n, x):
    dp = [[0 for _ in range(x+1)] for _ in range(n+1)]
    for j in range(1, min(x, m)+1):
        dp[1][j] = 1

    for i in range(2, n+1):
        for j in range(1, x+1):
            for k in range(1, min(j,m)+1):
                dp[i][j] += dp[i-1][j-k]

    return dp[n][x]

print(noOfWays(38, 7, 42))
