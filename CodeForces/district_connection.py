for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    no = True
    zeroth = arr[0]
    for i in arr:
        if i!=zeroth:
            no = False
            break
    if no:
        print('NO')
    else:
        print('YES')
        alr_con = [False]*n
        for i in range(n):
            assigned = False
            for j in range(i+1, n):
                if (not alr_con[j] or not alr_con[i]) and arr[j]!=arr[i]:
                    alr_con[i] = True
                    alr_con[j] = True
                    assigned = True
                    print(i+1, j+1)
            if not assigned:
                break
