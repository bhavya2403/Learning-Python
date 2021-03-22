for _ in range(int(input())):
    w1, w2, x1, x2, m = map(int, input().split())
    if x1*m <= w2-w1 <= x2*m:
        print(1)
    else:
        print(0)