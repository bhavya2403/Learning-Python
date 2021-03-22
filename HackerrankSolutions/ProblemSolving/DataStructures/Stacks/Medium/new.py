def twoStacks(s, a, b):
    ia = 0
    ib = 0
    rem_sum = 0
    count = 0
    broken = False
    while ia < len(a) and ib < len(b):
        if a[ia] <= b[ib]:
            for k in range():
                rem_sum += a[ia]
                ia += 1
                count += 1
        elif a[ia] > b[ib]:
            rem_sum += b[ib]
            ib += 1
            count += 1

        if rem_sum > s:
            broken = True
            break
    if broken:
        return count - 1

    while ia < len(a):
        if rem_sum + a[ia] > s:
            return count
        rem_sum += a[ia]
        ia += 1
        count += 1
    while ib < len(b):
        if rem_sum + b[ib] > s:
            return count
        rem_sum += b[ib]
        ib += 1
        count += 1
    return count


# print(twoStacks(10, 5, 4, [4,2,4,6,1], [2,1,8,5]))
for g_itr in range(int(input())):
    n,m,x = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    print(twoStacks(x, a, b))
