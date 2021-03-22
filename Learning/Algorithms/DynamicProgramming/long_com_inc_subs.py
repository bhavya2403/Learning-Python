def longestCommonIS(a, b):
    n1, n2 = len(a), len(b)
    # not working because problem in 13th line
    dp = [[(0,min(min(a),min(b))-1) for _ in range(n2)] for _ in range(n1)]

    for i in range(n1):
        for j in range(n2):
            if a[i] == b[j]:
                if i and j:
                    if dp[i-1][j-1][1] < a[i]:
                        dp[i][j] = dp[i-1][j-1][0]+1, a[i]
                    else:
                        dp[i][j] = dp[i-1][j-1][0], a[i] # ?????????
                else:
                    dp[i][j] = (1,a[i])

            elif i and j:
                if dp[i-1][j][0] >= dp[i][j-1][0]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
            elif i:
                dp[i][j] = dp[i-1][j]
            elif j:
                dp[i][j] = dp[i][j - 1]

    return dp[n1-1][n2-1][0]


from random import randint
print(longestCommonIS([randint(1,10) for _ in range(10)], [randint(1,10) for _ in range(10)]))