for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    while not k%2:
        k = k/2
    flag = 0
    for i in range(n):
        if arr[i]%k:
            flag = 1
            print('NO')
            break
    if not flag:
        print('YES')

