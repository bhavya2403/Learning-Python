for _ in range(int(input())):
    x, y = map(int, input().split())
    if x==3 and y==2:
        tot = 1
    elif y < 2 or x < 3:
        tot = 0
    else:
        tot = 0
        b = min(y, x-1)
        while b-1:
            num = x // (b+1)
            if num >= b-1:
                tot += int(b*(b-1)/2)
                break
            now = min(b-1, num)
            newB = x//(now+1)
            if b==newB:
                tot += now
                b -= 1
            else:
                tot += (b-newB)*now
                b = newB
    print(tot)
