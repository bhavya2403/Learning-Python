def lcsRecursive(s1,s2): # recursion O(2^mn)
    m, n = len(s1), len(s2)

    def solve(i, j):
        if i == m or j == n:
            return 0
        elif s1[i]==s2[j]:
            return 1 + solve(i+1, j+1)
        return max(solve(i+1, j), solve(i, j+1))

    return solve(0, 0)


def LCSMem(s1, s2): # O(m*n), whereas recursion was taking O(2^nm)
    m, n = len(s1), len(s2)
    matrix = [[-1 for _ in range(n+1)] for _ in range(m+1)]

    def solve(i, j):
        if i == m or j == n:
            return 0
        elif s1[i] == s2[j]:
            if matrix[i + 1][j + 1] == -1:
                matrix[i+1][j+1] = solve(i + 1, j + 1)
            return matrix[i+1][j+1] + 1

        if matrix[i + 1][j] == -1:
            matrix[i+1][j] = solve(i + 1, j)
        if matrix[i][j + 1] == -1:
            matrix[i][j+1] = solve(i, j + 1)

        return max(matrix[i+1][j], matrix[i][j+1])

    return solve(0, 0)


def LCSTab(s1, s2):
    n1, n2 = len(s1), len(s2)
    matrix = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    lu = set()
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                lu.add((i, j))
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    i, j = n1, n2
    arr, idx1, idx2 = [], [], []
    while i and j:
        if (i, j) in lu:
            arr.append(s1[i-1])
            idx1.append(i)
            idx2.append(j)
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i-1][j]:
            i -= 1
        else:
            j -= 1
    arr.reverse()
    idx1.reverse()
    idx2.reverse()

    return arr, idx1, idx2

print(LCSMem("ecfbefdcfca", "badfcbebbf"))
print(LCSTab("ecfbefdcfca", "badfcbebbf"))
