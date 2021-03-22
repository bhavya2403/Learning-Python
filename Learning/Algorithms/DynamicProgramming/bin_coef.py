def binomialCoefficient(n, k):
    ans = 1
    k = min(k, n-k)
    for i in range(k):
        ans *= (n-i)/(k-i)

    return round(ans)


print(binomialCoefficient(1000,500))
