def binary_search_ex(arr, value):
    arr.sort()
    left_idx = 0
    right_idx = len(arr) - 1
    arr.sort()
    s = ''

    while right_idx >= left_idx:
        i = (left_idx + right_idx) // 2

        if arr[i] > value:
            right_idx = i - 1

        elif arr[i] < value:
            left_idx = i + 1

        else:
            s = str(i)
            for j in range(i + 1, len(arr)):
                if arr[j] == arr[i]:
                    s += ', ' + str(j)
                else:
                    break
            j = i - 1
            while j > -1:
                if arr[j] == arr[i]:
                    s += ', ' + str(j)
                else:
                    return s
                j -= 1


numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
print(binary_search_ex(numbers, 15))
