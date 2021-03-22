for _ in range(int(input())):
    n, k = map(int, input().split())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x,y))
    broken1 = False
    for i in range(n):
        xi, yi = points[i]
        broken = False
        for j in range(n):
            xj, yj = points[j]
            if abs(xi-xj) + abs(yi-yj) > k:
                broken = True
                break
        if not broken:
            print(1)
            broken1 = True
            break
    if not broken1:
        print(-1)
