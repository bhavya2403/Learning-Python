def solveTab(n, arr):
    mini = min(arr)
    lookup = [0] * (n-mini+1)
    length = len(lookup)
    for i in range(length):
        ways = 0
        for num in arr:
            ways += lookup[i-num]
            if num >= i+mini:
                break
        lookup[i] = ways if i+mini not in arr else ways+1
    return lookup[length-1]

def solveMem(n, arr, mini):
    global lookupMem
    ways = 0
    for i in arr:
        if i > n:
            lookupMem[n] = ways
            return ways
        elif i == n:
            lookupMem[n] = ways+1
            return ways+1

        if not lookupMem[n-mini]:
            ways += solveMem(n-i, arr, mini)
        else:
            ways += lookupMem[n-i]

    lookupMem[n] = ways
    return ways

def total(n, arr):
    global lookupMem

    lookupMem = [0] * (n-min(arr)+2)
    return solveMem(n, arr, min(arr)), solveTab(n, arr)


print(total(30, [1,3,5,7,9,11,13,15,17,19,21]))