def superReduced(s):
    arr = []
    for i in s:
        arr.append(i)

    complete = False
    while not complete:
        found = False
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1] != 0:
                arr[i] = 0
                arr[i + 1] = 0
                found = True
        index = 0
        while index < len(arr):
            if arr[index] == 0:
                arr.remove(arr[index])
            else:
                index += 1
        if not found:
            complete = True

    s = ''
    for i in arr:
        s += str(i)

    if len(s) == 0:
        return 'Empty String'

    return s


print(superReduced('abbabaaaabb'))