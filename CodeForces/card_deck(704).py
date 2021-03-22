import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    maxIdx = [0] * n
    idx = 0
    for i in range(n):
        if arr[i] > arr[idx]:
            idx = i
        maxIdx[i] = idx

    r = n-1
    while True:
        l = maxIdx[r]

        for i in range(l, r+1):
            print(arr[i], end=' ')

        if not l:
            break
        r = l-1
        l = maxIdx[r]

    print()
