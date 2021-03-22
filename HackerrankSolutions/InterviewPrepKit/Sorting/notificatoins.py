def activityNotifications(n, expenditure, d):
    not_count = 0
    i = d + 1
    arr = sorted(expenditure)
    while i < n:
        arr1 = arr[i - d - 1:i - 1]
        if d % 2 == 1:
            median = arr1[d // 2]
        else:
            median = (arr1[d // 2] + arr1[(d // 2) - 1]) / 2

        if expenditure[i-1] >= 2 * median:
            not_count += 1
        i += 1
    return not_count


print(activityNotifications(9, [2,3,4,2,3,6,8,4,5], 5))
# nd = input().split()
# n = int(nd[0])
# d = int(nd[1])
# expenditure = list(map(int, input().rstrip().split()))
# print(activityNotifications(n, expenditure, d))