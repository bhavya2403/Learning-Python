def T(k, n):
    k = k % ((n//2)*n)
    lastLost = (k-1)//(n//2) + 1
    if not lastLost%2:
        at = n//2 + lastLost//2 + 1
    else:
        at = lastLost//2 + 1
    if not (at + ((k-1)%(n//2))) % n:
        return (at + ((k-1)%(n//2)))
    return (at + ((k-1)%(n//2))) % n


for _ in range(int(input())):
    n, k = map(int, input().split())

    if not n%2:
        if not k%n:
            print(n)
        else:
            print(k%n)
    else:
        print(T(k, n))
