def min_swaps(x, y, arr):
    summ = 0
    i = 0
    for i, num in enumerate(arr):
        summ += num
        if summ > y:
            break
        if x <= summ <= y:
            return 0
    if summ < x:
        return -1
    left_arr = arr[:i-1].sort()
    right_arr = arr[i:].sort()
    reference = left_arr + right_arr
    swaps = 1
    more_p_needed = [x-summ, y-summ]

