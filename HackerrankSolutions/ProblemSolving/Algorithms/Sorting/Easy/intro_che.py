def introTutorial(V, arr):
    size = len(arr)
    left_idx = 0
    right_idx = size-1
    while True:
        mid_idx = (left_idx+right_idx)//2
        if arr[mid_idx] > V:
            right_idx = mid_idx - 1
        elif arr[mid_idx] < V:
            left_idx = mid_idx + 1
        else:
            return mid_idx

print(introTutorial(23, [1, 3, 5, 7, 9, 11, 13, 15, 17 ,19 ,21 ,23]))