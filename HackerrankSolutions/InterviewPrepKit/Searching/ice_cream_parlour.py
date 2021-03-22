def whatFlavors(arr, m):
    d = {}
    if m%2 == 1:
        for i, ele in enumerate(arr):
            d[ele] = i
    else:
        for i, ele in enumerate(arr):
            if ele==m/2:
                if ele not in d:
                    d[ele] = i
                else:
                    return str(d[ele]+1) + ' ' + str(i+1)
            d[ele] = i
    for ele in d:
        if ele==m/2:
            continue
        if m-ele in d:
            return str(d[ele]+1) + ' ' + str(d[m-ele]+1)


print(whatFlavors([4,3,2,5,7], 8))