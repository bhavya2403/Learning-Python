def sumAreas(n, arr):
    arr.sort(reverse=True)
    pairTwo, pairFour = set(), set()
    i = 0
    while i < n:
        if arr[i]==arr[i+1]:
            if arr[i] in pairTwo:
                pairFour.add(arr[i])
            else:
                pairTwo.add(arr[i])
            i += 1
        elif arr[i]==arr[i+1]+1:
            if arr[i+1] in pairTwo:
                pairFour.add(arr[i+1])
            else:
                pairTwo.add(arr[i+1])
            i += 1
        i += 1
    totArea = 0
    for l in pairFour:
        totArea += l*l
    pairTwo = list(pairTwo)
    n = len(pairTwo)
    for i in range(n-1):
        for j in range(i+1, n):
            totArea += pairTwo[i] * pairTwo[j]

    return totArea


print(sumAreas(4, [3, 4, 5, 6]))