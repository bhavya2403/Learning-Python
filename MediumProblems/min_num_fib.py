def minNum(n):
    arr = [1, 1]
    a, b = 1, 1
    len = 2
    while a + b <= n:
        arr.append(a + b)
        a, b = a + b, a
        len += 1

    dp = [[0 for _ in range(n+1)] for _ in range(len+1)]
    summ = 0
    for j in range(1, n+1):
        dp[0][j] = len+1
    for i in range(1, len+1):
        summ += arr[i-1]
        for j in range(1, n+1):
            if summ < j:
                dp[i][j] = len+1
            else:
                dp[i][j] = min(1+dp[i-1][j-arr[i-1]], dp[i-1][j])

    return dp[len][n]


print(minNum(7))
