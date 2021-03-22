# we can use memoization in the recursive sol, O(nw), space: O(nw)
def solve1(m, leftCap, w, p, n):
    if n==0 or leftCap==0:
        return 0
    if m[n][leftCap-1] == -1:
        if w[n] > leftCap:
            m[n][leftCap-1] = solve1(m, leftCap, w, p, n-1)
        else:
            m[n][leftCap-1] = max(p[n]+solve1(m, leftCap-w[n], w, p, n-1), solve1(m, leftCap, w, p, n-1))

    return m[n][leftCap - 1]
# __________________________________________________
# we can also use tabulation which avoids recursion, O(nw), space: O(nw)
def solve2(w, p, capacity):
    n = len(w)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+p[i-1])
            else:
                dp[i][j] = dp[i-1][j]

    i, j = n, capacity
    while i:
        if dp[i][j] == dp[i-1][j]:
            w[i-1]=0
        else:
            j -= w[i-1]
            w[i-1] = 1
        i -= 1
    return w

# __________________________________________________
def knapsack(w, p, cap):
    n = len(w)
    m = [[-1 for _ in range(cap)] for _ in range(n)]
    return solve1(m, cap, w, p, n-1), solve2(w, p, cap)

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
print(knapsack(wt, val, W))
