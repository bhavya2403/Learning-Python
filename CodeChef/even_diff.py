for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    odds, evens = 0,0
    for i in arr:
        if i%2:
            odds += 1
        else:
            evens += 1
    print(min(odds, evens))