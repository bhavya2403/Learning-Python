for _ in range(int(input())):
    c = int(input())
    power = 0
    while 2**power <= c:
        power += 1
    s = ''
    for i in range(power-1, -1, -1):
        if c>= 2**i:
            c -= 2**i
            s += '1'
        else:
            s += '0'

    a, b = 2**power-1, 2**(power-1)-1
    for i in range(1, power):
        if s[i]=='1':
            a -= 2**(power-1-i)

    print(a*b)
