def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'NO'
    t = (x2-x1)/(v1-v2)
    if t in range(1, 1000000):
        return 'YES'
    return 'NO'