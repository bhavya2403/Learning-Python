def solve(m, arr):
    global dp

    for i in arr:
        if i > m:
            break
        elif i==m:
            dp[m] = [dp[m][0]+1, dp[m][1]+[[m]]]
            break

        if not dp[m-i][0]:
            dp[m-i] = solve(m-i, arr)

        for j in dp[m-i][1]:
            dp[m][1].append(j + [i])
        dp[m][0] += dp[m-i][0]

    return dp[m]


def subarraySum(m, arr):
    global dp

    dp = [[0, []] for _ in range(m+1)]
    arr.sort()

    return solve(m, arr)

print(subarraySum(10, [1,2,3,4,5]))

