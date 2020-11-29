def arrayManipulation(n, q):
    arr = [0 for i in range(1, n+1)]
    for i in q:
        for j in range(i[0], i[1]+1):
            arr[j-1] += i[2]

    return max(arr)


print(arrayManipulation(5, [[1,2,100], [2,5,100], [3,4,100]]))
