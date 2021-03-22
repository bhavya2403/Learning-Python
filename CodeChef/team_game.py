for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    firstL, lastL, notGood = set(), set(), []
    for i in arr:
        if i[0:1] not in firstL:
            firstL.add(i[0:1])
        if i[1:] not in lastL:
            lastL.add(i[1:])
    arr = set(arr)
    for i in firstL:
        for j in lastL:
            if i+j not in arr:
                notGood.append(i+j)

    l = len(notGood)
    count = 0
    for i in range(l-1):
        for j in range(i+1, l):
            if notGood[i][0:1]+notGood[j][1:] in arr and notGood[j][0:1]+notGood[i][1:] in arr:
                count += 2
    print(count)
