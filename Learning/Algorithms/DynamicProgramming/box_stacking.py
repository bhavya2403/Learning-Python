def boxStacking(arr, n):
    for i in range(n):
        (a, b, c) = arr[i]
        arr += [(b,c,a), (c,a,b)]

    arr.sort(key=lambda a:a[0]*a[1])
    n *= 3

    lis = [i[2] for i in arr]
    for i in range(1, n):
        l1, b1 = min(arr[i][0], arr[i][1]), max(arr[i][0], arr[i][1])
        for j in range(i):
            l2, b2 = min(arr[j][0], arr[j][1]), max(arr[j][0], arr[j][1])
            if l2<l1 and b2<b1 and lis[i]<lis[j]+arr[i][2]:
                lis[i] = lis[j] + arr[i][2]

    return max(lis)

arr = [(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)]
print(boxStacking(arr, len(arr)))