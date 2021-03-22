for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    maxA = max(a)
    maxIdx = a.index(maxA)
    for i in range(n):
        if i==maxIdx:
            continue
        k = b[i]/A if not b[i]%A else int(b[i]/A)+1
        B -= k*(a[i])
        if B <= 0:
            break
    if B:
        i = maxIdx
        k = b[i] / A if not b[i] % A else int(b[i] / A) + 1
        B -= k * (a[i])
        if B <= -a[i]:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
