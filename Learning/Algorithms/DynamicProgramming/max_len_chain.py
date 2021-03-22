class air(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def maxChainLen(arr, n):
    lis = [1] * n
    arr.sort(key=lambda obj: obj.a)
    for i in range(n):
        for j in range(i):
            if arr[i].a > arr[j].b and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)


tcs = int(input())
for _ in range(tcs):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr1 = []
    i = 0
    while n * 2 > i:
        arr.append(air(arr1[i], arr1[i + 1]))
        i += 2
    print(maxChainLen(arr, n))
