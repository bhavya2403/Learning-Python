def LPS(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    def solve(i, j):
        if not dp[i][j]:
            if i==j:
                dp[i][i] = 1

            elif i==j-1:
                if string[i]==string[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1

            elif string[i] == string[j]:
                dp[i][j] = 2 + solve(i+1, j-1)

            else:
                dp[i][j] = max(solve(i+1, j), solve(i, j-1))

        return dp[i][j]

    ans = solve(0, n-1)
    return ans

print(LPS("BBABCBCAB"))
