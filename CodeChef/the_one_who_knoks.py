for i in range(int(input())):
    ar = input().split()
    x = int(ar[0])
    y = int(ar[1])
    z = y - x
    if z > 0:
        if z % 4 == 0:
            print(3)
        elif z % 2 == 0:
            print(2)
        else:
            print(1)
    elif z < 0:
        print(1 if abs(z) % 2 == 0 else 2)
    else:
        print(0)

