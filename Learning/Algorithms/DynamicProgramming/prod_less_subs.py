def countSubs(arr, k):
    n = len(arr)
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            if i >= arr[j-1]:
                dp[i][j] += dp[i//(arr[j-1])][j-1] + 1

    return dp[k][n]

print(countSubs([1,2,3,4],10))
