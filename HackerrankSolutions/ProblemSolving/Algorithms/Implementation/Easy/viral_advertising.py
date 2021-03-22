def viralAdvertising(n):
    shared = 5
    cumulative = 2
    for day in range(2, n+1):
        shared = (shared // 2) * 3
        cumulative += shared // 2

    return cumulative


print(viralAdvertising(5))
