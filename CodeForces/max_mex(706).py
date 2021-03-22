from math import ceil

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if not k:
        print(n)
    else:
        moreInA = False
        for i in a:
            if i > n-1:
                moreInA = True
                break
        if not moreInA:
            print(n+k)
        else:
            a.sort()
            i = 0
            for idx in range(n):
                if idx != a[idx]:
                    i = idx
                    break

            if ceil((i+max(a))/2) in set(a):
                print(n)
            else:
                print(n+1)
