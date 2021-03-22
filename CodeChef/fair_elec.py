for _ in range(int(input())):
    lena, lenb = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    count = 0
    possible = False
    while count <= min(lena, lenb)+1:
        sumA, sumB = sum(a), sum(b)
        if sumA > sumB:
            possible = True
            print(count)
            break
        minA, maxB = min(a), max(b)
        if minA >= maxB:
            print(-1)
            break
        min_idx, max_idx = a.index(minA), b.index(maxB)
        a[min_idx], b[max_idx] = maxB, minA
        count += 1

