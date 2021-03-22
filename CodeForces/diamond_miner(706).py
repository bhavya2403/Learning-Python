from math import sqrt

for _ in range(int(input())):
    n = int(input())
    miners, mines = [], []
    for _ in range(2*n):
        x, y = map(int, input().split())
        if not x:
            miners.append(y)
        else:
            mines.append(x)

    miners.sort(key=lambda n:abs(n))
    mines.sort(key=lambda n:abs(n))

    print(sum(sqrt(miners[i]*miners[i] + mines[i]*mines[i]) for i in range(n)))
