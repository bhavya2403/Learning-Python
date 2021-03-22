def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        arr[query[0] - 1] += query[2]
        arr[query[1]] -= query[2]

    maximum = 0
    count = 0
    for i in arr:
        count += i
        if count > maximum:
            maximum = count

    return maximum
