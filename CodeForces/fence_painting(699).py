def solve(n, m, a, b, c):
    weNeedDict = {}
    for i in range(n):
        if a[i] != b[i]:
            if b[i] not in weNeedDict:
                weNeedDict[b[i]] = [i]
            else:
                weNeedDict[b[i]].append(i)
    avail = {}
    for i in c:
        if i not in avail:
            avail[i] = 1
        else:
            avail[i] += 1

    for i in weNeedDict:
        if i not in avail:
            return False
        if avail[i] < len(weNeedDict[i]):
            return False
    if c[m-1] not in set(b):
        return False
    if c[m-1] not in weNeedDict:
        lastPos = b.index(c[m-1])+1
    else:
        lastPos = weNeedDict[c[m-1]][0]+1
    answer = []
    for i in c:
        if i in weNeedDict:
            pos = weNeedDict[i].pop()
            answer.append(pos+1)
            if not weNeedDict[i]:
                weNeedDict.__delitem__(i)
        else:
            answer.append(lastPos)
    return answer


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    answer = solve(n, m, a, b, c)
    if answer:
        print('YES')
        for i in answer:
            print(i, end=' ')
        print()
    else:
        print('NO')
