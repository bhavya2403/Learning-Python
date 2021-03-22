for _ in range(int(input())):
    n, m, k = map(int, input().split())

    n, m = min(m, n), max(m, n)
    if not n%2:
        xor = (k + 2) ^ (k + 2 + m)
        for i in range(1, int(n/2)):
            xor ^= k+2*(i+1)
            xor ^= k+2*(i+1)+m
    else:
        xor = (k+3)^(k+3+m)
        for i in range(1, int(n/2)):
            xor ^= k+2*(i+1)+1
            xor ^= k+2*(i+1)+1+m
        for i in range(m):
            xor ^= k+(i+2)

    print(xor)