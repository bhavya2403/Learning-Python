import sys

t = sys.stdin.readline()
t = int(t)
for _ in range(t):
    x, y = sys.stdin.readline().split()
    chef = True
    if y == '1':
        if len(x)>1:
            chef = False
        else:
            if int(x) > 2:
                chef = False
    else:
        x, y = int(x), int(y)
        chef = True
        arr = [0] * (x + 1)
        primes = 0
        for i in range(2, x + 1):
            if not arr[x]:
                j = 2 * i
                while j <= x:
                    arr[j] = 1
                    j += x
                primes += 1
            if primes > y:
                chef = False

    if chef:
        print('Chef')
    else:
        print('Divyam')
