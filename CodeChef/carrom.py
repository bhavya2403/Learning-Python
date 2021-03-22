for _ in range(int(input())):
    n, k, x, y = map(int, input().split())
    if x == y:
        print(n, n)
    else:
        need = n - max(x, y)
        col1 = [x + need, y + need]
        col2 = [col1[1], col1[0]]
        need = min(col2)
        col3 = [col2[0]-need, col2[1]-need]
        col4 = [col3[1], col3[0]]
        if k > 4:
            k = k % 4
        if k == 1:
            print(col1[0], col1[1])
        elif k == 2:
            print(col2[0], col2[1])
        elif k == 3:
            print(col3[0], col3[1])
        elif k == 4:
            print(col4[0], col4[1])

