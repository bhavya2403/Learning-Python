def picnicGroups(arr):
    count = 0
    onces, twos, threes = 0, 0, 0
    for i in arr:
        if i==2:
            twos += 1
        elif i==1:
            onces += 1
        elif i==3:
            threes += 1
        else:
            count += 1

    count += threes
    onces -= threes
    count += twos // 2 + twos % 2
    if onces > 0:
        if twos%2:
            onces -= 2
        count += onces//4 + (1 if onces%4 else 0)

    return count


print(picnicGroups([2,3,3,4,3,3]))
