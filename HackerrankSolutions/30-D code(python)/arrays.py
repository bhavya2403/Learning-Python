def reverse(arr):
    arr1 = []
    for i in arr:
        arr1.insert(0, i)
    s = str(arr1[0])
    for i in range(1, len(arr1)):
        s += ' ' + str(arr1[i])

    return s
