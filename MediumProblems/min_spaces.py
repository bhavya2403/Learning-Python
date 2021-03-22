# https://www.youtube.com/watch?v=tOD6g7rF7NA&t=881s

def minSpaces(string, arr):
    n = len(arr)
    m = len(string)
    dp = [-1] * (m+1)
    dp[m] = 0

    def solve(i):
        if dp[i] == -1:
            indices = [j for j in range(n) if arr[j]==string[i:i+len(arr[j])]]
            if not indices:
                dp[i] = 1000
            else:
                dp[i] = 1 + min((solve(i+len(arr[j]))  for j in indices))

        return dp[i]

    return solve(0)


print(minSpaces('3141592653589793238462643383279', ['314', '159', '49', '9001', '15926535897','14', '9323', '8462643383279', '4', '793'])-1)
