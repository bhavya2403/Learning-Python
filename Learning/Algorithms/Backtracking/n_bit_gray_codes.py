def solve(notTaken, strArr, answer, num, n):
    if not notTaken:
        print(answer)
        return

    for i in range(n):
        if not strArr[i]:
            strArr[i]=1
            num += 2**(n-i-1)
            if num in notTaken:
                solve(notTaken-{num}, strArr, answer+[num], num, n)
            strArr[i] = 0
            num -= 2**(n-i-1)
        else:
            strArr[i]=0
            num -= 2**(n-i-1)
            if num in notTaken:
                solve(notTaken-{num}, strArr, answer+[num], num, n)
            strArr[i] = 1
            num += 2**(n-i-1)

def nBitGrayCodes(n):
    return solve({i for i in range(1, 2**n)}, [0 for _ in range(n)], [0], 0, n)

nBitGrayCodes(4)
