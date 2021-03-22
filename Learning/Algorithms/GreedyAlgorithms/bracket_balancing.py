for _ in range(int(input())):
    n = int(input())
    s = input()
    swaps = 0
    pos = []
    for i in range(n):
        if s[i]=='[':
            pos.append(i)

    p = 0
    oc, cc = 0, 0
    s = list(s)
    for i in range(n):
        if s[i]=='[':
            oc += 1
            p += 1
        else:
            cc += 1
        if cc > oc:
            swaps += pos[p]-i
            s[i], s[pos[p]] = '[', ']'
            p += 1
            oc += 1
            cc -= 1
    print(swaps)