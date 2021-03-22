def rotateLeft(d, arr):
    if d >= len(arr):
        d = d % len(arr)
    for i in range(d):
        temp = arr[0]
        arr.remove(arr[0])
        arr.append(temp)

    return arr