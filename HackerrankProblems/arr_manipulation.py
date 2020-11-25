def araManipulation(n, q):
    arr = [0 for i in range(1, n+1)]
    for i in q:
        for j in range(i[0], i[1]+1):
            arr[j-1] += i[2]

    return max(arr)


araManipulation(10, [[1,5,3],[4,8,7],[6,9,1]])

