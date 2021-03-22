def evenLenBinary(n):
    m = 10**9 + 7
    half = n//2 + 1
    ncr = 1
    res = 1
    for r in range(1, half):
        ncr = ((n-r+1)*ncr)//r
        res += ncr*ncr
    res *= 2
    if not n%2:
        res -= ncr*ncr

    return res % m


print(evenLenBinary(100000))