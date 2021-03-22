def boxes(n, k, arr):
    arr.sort()
    i = n-1
    suum1 = 0
    count = 0
    while i >= 0:
        count += 1
        suum1 += arr[i]
        arr[i] = 0
        if suum1 >= k:
            break
        i -= 2
    if suum1 < k:
        return -1
    suum2 = sum(arr[i+1:])
    count += count-1
    while i > 0:
        i -= 1
        suum2 += arr[i]
        count += 1
        if suum2 >= k:
            return count

    return -1

# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     print(boxes(n, k, arr))

print(boxes(3, 3, [1,5,2]))