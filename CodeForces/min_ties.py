for _ in range(int(input())):
    n = int(input())
    win = [0] * n
    lose = [0] * n
    if n==2:
        print(0, end='')
    else:
        maxWins = (n-1)//2
        i, j = 1, 2
        while i!=n:
            if i==j-1 and not n%2 and i%2:
                print(0, end=' ')
            elif win[i-1] < maxWins and lose[j-1] < maxWins:
                print(1, end=' ')
                win[i-1] += 1
                lose[j-1] += 1
            else:
                print(-1, end=' ')
                win[j-1] += 1
                lose[i-1] += 1
            j += 1
            if j==n+1:
                i += 1
                j = i+1
    print()
