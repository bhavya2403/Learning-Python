for _ in range(int(input())):
    s = input()
    cont = False
    tot = 0
    for i in s:
        if i=='0':
            cont = False
        else:
            if not cont:
                cont = True
                tot += 1
    print(tot)