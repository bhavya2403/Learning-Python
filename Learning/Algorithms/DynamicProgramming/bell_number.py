def bell(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if not j or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = (j+1)*dp[i-1][j] + dp[i-1][j-1]
    return sum(dp[n-1][j] for j in range(n))

print(bell(5))