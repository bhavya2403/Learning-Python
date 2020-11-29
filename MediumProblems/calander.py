def spare_time(cal, bound):
    cal.insert(0, [0, bound[0]])
    cal.append([bound[1], 0])

    ar = []
    for i in cal:
        for j in i:
            ar.append(j)

    ar1 = []
    index = 0
    while True:
        if index < len(ar)-2:
            if ar[index+1] != ar[index+2]:
                ar1.append([ar[index+1], ar[index+2]])
        elif index == len(ar)-2:
            break
        index += 2
    print(ar1)
    return ar1


def time_ava_for_meet(ar1, ar2):
    ar3 = []
    for i in ar1:
        for j in ar2:
            if i[0] < j[0] < i[1]:
                ar3.append([j[0], min(j[1], i[1])])
            if j[0] < i[0] < j[1]:
                ar3.append([i[0], min(j[1], i[1])])

    if all(ar3.count(i) == 1 for i in ar3):
        return ar3
    else:
        uniques = []
        for i in ar3:
            if i not in uniques:
                uniques.append(i)
        return uniques


print(time_ava_for_meet(spare_time([[9.00, 10.30], [12.00, 13.00], [16.00, 18.00]], [9.00, 20.00]), spare_time([[10.00, 11.30], [12.30, 14.30], [14.30, 15.00], [16.00, 17.00]], [10.00, 18.30])))
