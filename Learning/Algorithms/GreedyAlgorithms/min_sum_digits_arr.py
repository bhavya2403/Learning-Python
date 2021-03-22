def minSum(a):
    n = len(a)
    a.sort()
    raised = (n // 2) - 1
    n1, n2 = 0, 0
    if not n % 2:
        for i in range(n // 2):
            n1 += (10 ** raised) * a[2 * i]
            n2 += (10 ** raised) * a[2 * i + 1]
            raised -= 1
    else:
        for i in range(n // 2):
            n1 += (10 ** (raised + 1)) * a[2 * i]
            n2 += (10 ** raised) * a[2 * i + 1]
            raised -= 1
        n1 += a[n - 1]
    return n1 + n2


print(minSum([3, 4, 7, 5, 0]))
