def flatlandSpaceStations(n, c):
    c.sort()
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    maxi = c[0]
    size = len(c)
    for i in range(1, size):
        max_dist = int(((c[i] + c[i - 1]) / 2) - c[i - 1])
        if max_dist > maxi:
            maxi = max_dist

    max_dist = n-c[size-1]-1
    if max_dist > maxi:
        maxi = max_dist

    return maxi


print(flatlandSpaceStations(20, [13,11,10,7]))
