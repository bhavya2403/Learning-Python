romanDict = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}
for i in range(3):
    romanDict[4*(10**i)] = romanDict[10**i] + romanDict[5*(10**i)]
    romanDict[9*(10**i)] = romanDict[10**i] + romanDict[10**(i+1)]

arr = sorted([i for i in romanDict])
ptr = -1
for num in range(1, 1001):
    if num in romanDict:
        ptr += 1
        ans = romanDict[num]
    else:
        j = ptr
        ans = ''
        n = num
        while n:
            ans += (n//arr[j])*(romanDict[arr[j]])
            n %= arr[j]
            j -= 1
    print(num, '-', ans)
