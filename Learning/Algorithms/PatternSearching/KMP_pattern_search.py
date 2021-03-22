def computeLPS(substr, m):  # length of prefix that is also a suffix (O(m))
    # lps is used when we get a mismatch we don't directly set j to zero
    lps = [0 for _ in range(m)]
    i, j = 1, 0
    while i < m:
        if substr[j] == substr[i]:
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return lps


def KMPSearch(str, substr):  # O(n)
    n, m, result = len(str), len(substr), []
    lps = computeLPS(substr, m)
    i, j = 0, 0
    while i < n:
        if str[i] == substr[j]:
            i += 1
            j += 1
        else:
            if j:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            result.append(i - j)
            j = lps[j - 1]
    return result


print(computeLPS('aaaabaacd', 9))
print(KMPSearch('AAAAABAAABA', 'AAA'))
# overall time complexity: O(n+m) ~ O(n)
# space: O(m) (we need one extra array)
