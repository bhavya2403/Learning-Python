def divisibleSumPairs(n, k, ar):
    ways = 0
    for i in range(n):
        for j in range(n):
            if j > i and (ar[i] + ar[j]) % k == 0:
                ways += 1

    return ways


print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
