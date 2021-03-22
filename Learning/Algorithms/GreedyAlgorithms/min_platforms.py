def minimumPlatform(n, arrival, departure):
    arr = []
    for i in range(n):
        arr.append((arrival[i], 0))
        arr.append((departure[i], 1))
    arr.sort()

    curr_act, max_act = 0, 0
    for i in range(2 * n):
        if arr[i][1]:
            curr_act -= 1
        else:
            curr_act += 1
            if curr_act > max_act:
                max_act = curr_act

    return max_act


print(minimumPlatform(6, [900,940,950,1100,1500,1800], [910,1200,1120,1130,1900,2000]))