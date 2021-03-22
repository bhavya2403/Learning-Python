from util import time_it

@time_it
def binary_search(arr, value):
    left_idx = 0
    right_idx = len(arr)-1
    arr.sort()

    while right_idx >= left_idx:
        i = (left_idx + right_idx) // 2
        if arr[i] == value:
            return i
        elif arr[i] > value:
            right_idx = i - 1
        else:
            left_idx = i + 1

    return 'Value Not Found'


@time_it
def binary_search_recursive(left_idx, right_idx, arr, value):
    i = (left_idx + right_idx) // 2
    if left_idx==right_idx:
        if arr[i] == value:
            return i
        else:
            return 'value not found'
    else:
        if arr[i] == value:
            return i
        elif arr[i] > value:
            return binary_search_recursive(left_idx, i-1, arr, value)
        else:
            return binary_search_recursive(i+1, right_idx, arr, value)


# print(binary_search([i for i in range(10000001)], 12345))  # took 95ms
print(binary_search_recursive(0, 10000000, [i for i in range(10000001)], 1000000))
