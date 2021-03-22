class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def maxChainLen(arr, n):
    ans = [[(arr[i].a, arr[i].b)] for i in range(n)]

    lis = [1] * n
    arr.sort(key=lambda obj: obj.a)
    for i in range(n):
        for j in range(i):
            if arr[i].a > arr[j].b and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                ans[i] = ans[j] + [(arr[i].a, arr[i].b)]

    maxVal, maxIdx = 0, 0
    for i in range(n):
        if lis[i] > maxVal:
            maxVal = lis[i]
            maxIdx = i
    return ans[maxIdx]


tcs = int(input())
for _ in range(tcs):
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    arr = []
    i = 0
    while n * 2 > i:
        arr.append(Pair(arr1[i], arr1[i + 1]))
        i += 2
    print(maxChainLen(arr, n))
