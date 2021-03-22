def solve(m, arr, dp):

    for i in arr:
        if i > m:
            break
        elif i==m:
            dp[m] = (1, [m])
            break

        if dp[m-i][0] == 10000:
            dp[m-i] = solve(m-i, arr, dp)

        num = min(dp[m][0], dp[m-i][0]+1)
        if num == dp[m-i][0]+1:
            dp[m] = dp[m-i][0]+1, dp[m-i][1]+[i]

    return dp[m]


def subarraySum(m, arr):
    dp = [(10000, []) for _ in range(m+1)]
    arr.sort()

    return solve(m, arr, dp)

print(subarraySum(7, [2,3,5]))
