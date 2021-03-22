def cutTheSticks(arr):
    s = list(set(arr))
    s.sort()
    ar1 = [len(arr)]
    temp = len(arr)
    for i in range(len(s)-1):
        temp -= arr.count(s[i])
        ar1.append(temp)

    return ar1


print(cutTheSticks([5, 4, 4, 2, 2, 8]))
