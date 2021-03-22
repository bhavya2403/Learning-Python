def solve(curr, s, dp, lSum, lSet):
    if curr == len(s)-1:
        if lSum == sum(s)/2:
            print(lSet)
            return 1
        return 0

    if dp[curr + 1][lSum + s[curr]] == -1:
        dp[curr + 1][lSum + s[curr]] = solve(curr + 1, s, dp, lSum + s[curr], lSet+[s[curr]])

    if dp[curr + 1][lSum + s[curr]]:
        dp[curr][lSum] = 1
    else:
        if dp[curr + 1][lSum] == -1:
            dp[curr + 1][lSum] = solve(curr + 1, s, dp, lSum, lSet)
        if dp[curr + 1][lSum]:
            dp[curr][lSum] = 1
        else:
            dp[curr][lSum] = 0

    return dp[curr][lSum]


def partition(s):
    summ = sum(s)
    n = len(s)
    dp = [[-1 for _ in range(summ + 1)] for _ in range(n)]
    lRange = summ // 2 + 1
    for i in range(n):
        for j in range(lRange, summ + 1):
            dp[i][j] = 0

    s.sort()

    return solve(0, s, dp, 0, [])


from random import randint

for _ in range(10):
    print(partition([randint(1, 1000) for _ in range(100)]))
# print(partition([1,5,11,5]))