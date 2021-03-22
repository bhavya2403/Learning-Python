def solveMem(m, n, dp):
    if m==n==0:
        return 0
    if m==0 or n==0:
        return 1

    if dp[m-1][n]:
        sum1 = dp[m-1][n]
    else:
        sum1 = solve(m-1, n, dp)
        dp[m-1][n] = sum1

    if dp[m][n-1]:
        sum2 = dp[m][n-1]
    else:
        sum2 = solveMem(m, n-1, dp)
        dp[m][n-1] = sum2

    dp[m][n] = sum1+sum2
    return dp[m][n]

def gridTraveller(m, n):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    return solveMem(n-1, m-1, dp)

print(gridTraveller(18, 18))