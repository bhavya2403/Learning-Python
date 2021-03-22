def bruteForceSearch(str, substr): # O((n-m+1)*m) ~ O(mn)
    n = len(str)
    m = len(substr)
    for i in range(n-m+1):
        for j in range(m):
            if str[i+j] != substr[j]:
                break
            if j == m-1:
                return True

    return False

print(bruteForceSearch('This is a Test', 'Test'))