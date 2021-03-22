def eggDroppings(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    def solve(n, k):
        if n==1:
            return k
        if k==1 or k==0:
            return k

        min = 10000
        for x in range(1, k+1):
            if not dp[n][k-x]:
                dp[n][k-x] = solve(n, k-x)
            if not dp[n-1][x-1]:
                dp[n-1][x-1] = solve(n-1, x-1)

            res = max(dp[n][k-x], dp[n-1][x-1])
            if res < min:
                min = res
        return 1 + min

    return solve(n, k)


print(eggDroppings(2, 36))
