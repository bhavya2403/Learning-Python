def utopianTree(n):
    nthterm = 0
    count = 0
    while count <= n+1:
        if count % 2 == 0:
            nthterm = nthterm * 2
        else:
            nthterm += 1
        count += 1

    return nthterm


print(utopianTree(3))
