for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c0, c1, c2 = 0, 0, 0
    for i in range(n):
        if not a[i]%3:
            c0 += 1
        elif not a[i]%3-1:
            c1 += 1
        else:
            c2 += 1

    mid = n//3
    count = 0
    while not (c0==c1==c2):
        if c0 > mid:
            c1 += c0-mid
            count += c0-mid
            c0 = mid
        if c1 > mid:
            c2 += c1-mid
            count += c1-mid
            c1 = mid
        if c2 > mid:
            c0 += c2-mid
            count += c2-mid
            c2 = mid
    print(count)