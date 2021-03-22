def activityNotifications(n, expenditure, d):
    not_count = 0
    arr = sorted(expenditure[:d])
    expenditure[:d] = arr
    for i in range(d, n):
        num = expenditure[i]
        if d % 2 == 1:
            median = arr[d // 2]
        else:
            median = (arr[d // 2] + arr[(d // 2) - 1]) / 2

        if num >= 2 * median:
            not_count += 1

        arr.remove(expenditure[i-d])
        inserted = False
        for j in range(d-1):
            if arr[j] > num:
                inserted = True
                arr.insert(j-1, num)
        if not inserted:
            arr.append(num)
        i +=  1

    return not_count

nd = input().split()
n = int(nd[0])
d = int(nd[1])
expenditure = list(map(int, input().split()))
print(activityNotifications(n, expenditure, d))
# print(activityNotifications(9, [2,3,4,2,3,6,8,4,5], 5))
# print(activityNotifications(5, [10,20,30,40,50], 3))