def median(a, n):
    if n % 2:
        return a[n // 2]
    return (a[n // 2] + a[n // 2 - 1]) / 2


def medianLen1(num, b, n):
    if not n % 2:
        l, r = b[n // 2], b[n // 2 - 1]
        if num <= l:
            return l
        if l < num < r:
            return num
        return r
    m = b[n // 2]
    if num == m:
        return m
    if num < m:
        return (max(b[n // 2 - 1], num) + m) / 2
    return (m + min(b[n // 2 + 1], num)) / 2


def medianSorted(a, b, n1, n2):
    if n1 == 0 and n2 == 0:
        return -1
    elif n1 and not n2:
        return median(a, n1)
    elif n2 and not n1:
        return median(b, n2)
    elif n1 == 1 and n2 == 1:
        return (a[0] + b[0]) / 2
    elif n1 == 1:
        return medianLen1(a[0], b, n2)
    elif n2 == 1:
        return medianLen1(b[0], a, n1)
    elif n1 == 2 and n2 == 2:
        return (max(a[0], b[0]) + min(a[1], b[1])) / 2

    m1 = median(a, n1)
    m2 = median(b, n2)

    if m1 == m2:
        return m1
    if m1 > m2:
        if not n2 % 2:
            b = b[n2 // 2 - 1:]
        else:
            b = b[n2 // 2:]
        return medianSorted(a[:n1 // 2 + 1], b, n1 // 2 + 1, n2 // 2 + 1)
    if m1 < m2:
        if not n1 % 2:
            a = a[n1 // 2 - 1:]
        else:
            a = a[n1 // 2:]
        return medianSorted(a, b[:n2 // 2 + 1], n1 // 2 + 1, n2 // 2 + 1)


print(medianSorted([10.5], [4, 9, 10, 11, 13], 1, 5))
