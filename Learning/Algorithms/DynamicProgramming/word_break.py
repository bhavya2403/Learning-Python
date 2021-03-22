def wordBreak(string, words):
    k = max(len(s) for s in words)
    lookup = [set()] * k
    for word in words:
        for idx, char in enumerate(word):
            lookup[idx].add(word[:idx+1])
    n = len(string)
    dp = [-1] * n

    def solve(currIdx):
        if currIdx >= n:
            return True
        if dp[currIdx] != -1:
            return dp[currIdx]

        for i in range(currIdx, n):
            if i-currIdx >= k:
                dp[currIdx] = False
                break
            if string[currIdx:i+1] not in lookup[i-currIdx]:
                dp[currIdx] = False
                break

            if string[currIdx:i+1] in words:
                if solve(i+1):
                    dp[currIdx] = True
                    break

        return dp[currIdx]

    return solve(0)

print(wordBreak("ilikesamsungmobile", { "and", "i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}))
