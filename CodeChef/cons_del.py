for _ in range(int(input())):
    n, k = map(int, input().split())
    a = input().split()

    onces = 0
    for i in range(k):
        if a[i] == '1':
            onces += 1
    minOnces = onces
    minLTuple = (0, k-1)

    for i in range(k, n):
        if a[i] == '1':
            onces += 1
        if a[i-k] == '1':
            onces -= 1

        if onces < minOnces:
            minOnces = onces
            minLTuple = (i-k+1, i)

    cost = int(minOnces*(minOnces+1)/2)

    for i in range(minLTuple[0]):
        if a[i] == '1':
            cost += 1
    for i in range(minLTuple[1]+1, n):
        if a[i]=='1':
            cost += 1

    print(cost)
