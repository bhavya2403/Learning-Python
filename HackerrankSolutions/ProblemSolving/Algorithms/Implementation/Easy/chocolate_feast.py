def chocolateFeast(n, c, m):
    bought = wrappers = n // c
    while wrappers >= m:
        bought += 1
        wrappers = wrappers - m + 1

    return bought


print(chocolateFeast(6,2,2))