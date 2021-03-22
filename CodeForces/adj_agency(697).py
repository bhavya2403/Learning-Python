def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    result = 1
    if n > k:
        d = {}
        s = set()
        for i in a:
            if i not in d:
                d[i] = 1
                s.add(i)
            else:
                d[i] += 1
        s = sorted(list(s))
        s.reverse()
        for i in s:
            if k <= 0:
                break
            if d[i] <= k:
                k -= d[i]
            else:
                n = d[i]
                if 2*k > n:
                    k = n-k
                result = ncr(n, k, 10**9 + 7)
                break
    print(result)
