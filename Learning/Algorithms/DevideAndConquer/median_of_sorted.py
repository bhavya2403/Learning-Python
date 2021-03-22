def median(a):
    n = len(a)
    if n % 2:
        return a[n // 2]
    return (a[n // 2] + a[n // 2 - 1]) / 2


def medianSorted(a, b, n):
    if n == 0:
        return -1
    if n == 1:
        return (a[0] + b[0]) / 2
    if n == 2:
        return (max(a[0], b[0]) + min(a[1], b[1])) / 2

    m1 = median(a)
    m2 = median(b)

    if m1 == m2:
        return m1
    if m1 > m2:
        if not n % 2:
            return medianSorted(a[:n // 2 + 1], b[n // 2 - 1:], n // 2 + 1)
        return medianSorted(a[:n // 2 + 1], b[n // 2:], n // 2 + 1)
    if m1 < m2:
        if not n % 2:
            return medianSorted(a[n // 2 - 1:], b[:n // 2 + 1], n // 2 + 1)
        return medianSorted(a[n // 2:], b[:n // 2 + 1], n // 2 + 1)


print(medianSorted([2, 3, 5, 7, 11, 12], [4, 9, 10, 11, 13, 15], 6))
