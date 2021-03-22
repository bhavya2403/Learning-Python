def minValue( a, b, n):
    a1 = sorted(a)
    a2 = a1.copy()
    a2.reverse()
    b1 = sorted(b)
    b2 = b1.copy()
    b2.reverse()
    sum1, sum2 = 0, 0
    for i in range(n):
        sum1 += a1[i]*b2[i]
        sum2 += a2[i]*b1[i]
    return min(sum1, sum2)
