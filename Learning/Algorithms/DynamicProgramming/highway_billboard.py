def highwayBillboard(M, x, r, t):
    n = len(x)
    M = max(x)
    indexD = {x[i]:i for i in range(n)}

    dp = [0] * (M+1)
    for i in range(1, M+1):
        if i in indexD:
            if i < t-1:
                dp[i] = r[indexD[i]]
            else:
                dp[i] = max(dp[i-t-1]+r[indexD[i]], dp[i-1])
        else:
            dp[i] = dp[i-1]

    return dp[M]

print(highwayBillboard(15, [6, 9, 12, 14], [5, 6, 3, 7, 2], 2))
