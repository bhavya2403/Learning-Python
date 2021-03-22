from math import ceil

def friendsPairing(n):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1
    dp[1][0] = 1
    for i in range(1, n):
        for j in range(ceil(i/2)-1, i+1):
            if i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + (2*j-i+2)*dp[i-1][j]

    return sum(dp[n-1][j] for j in range(ceil(n/2)-1, n))

def friends(n):
    if n==1 or n==2:
        return n

    a, b = 2,1
    for i in range(3, n+1):
        a, b = a+(i-1)*b, a
    return a

print(friends(5))
print(friendsPairing(5))