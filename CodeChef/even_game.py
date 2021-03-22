for _ in range(int(input())):
    n = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr)%2:
        print(2)
    else:
        print(1)
