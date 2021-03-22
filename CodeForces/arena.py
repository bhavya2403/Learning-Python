for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    minEl, count = 101, 0
    for i in arr:
        if i < minEl:
            minEl = i
            count = 1
        elif i==minEl:
            count += 1
    print(n-count)
