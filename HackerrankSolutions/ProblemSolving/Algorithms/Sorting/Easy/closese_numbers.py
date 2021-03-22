def closestNumbers(arr):
    arr.sort()
    diff_arr = [arr[0], arr[1]]
    min_diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] < min_diff:
            diff_arr = [arr[i], arr[i + 1]]
            min_diff = arr[i + 1] - arr[i]
        elif arr[i + 1] - arr[i] == min_diff:
            diff_arr += [arr[i], arr[i + 1]]
    return diff_arr


print(closestNumbers([-20, -3916237, -357920, -7620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]))
