def adding(a, b, freqArr, arr, count):
    for i in range(a + 1, b + 1):
        if not freqArr[arr[i]]:
            count += 1
        freqArr[arr[i]] += 1
    return count, freqArr


def removing(x, y, freqArr, arr, count):
    if x[1] < y[0]:
        return adding(y[0], y[1], [0] * (10 ** 6), arr, 0)

    for i in range(x[0], y[0]):
        if freqArr[arr[i]] == 1:
            count -= 1
        freqArr[arr[i]] -= 1
    if x[1] > y[1]:
        for i in range(y[1] + 1, x[1] + 1):
            if freqArr[arr[i]] == 1:
                count -= 1
            freqArr[arr[i]] -= 1
    else:
        return adding(x[1], y[1], freqArr, arr, count)
    return count, freqArr


def mo(arr, queries, freq):
    freqArr = [0] * (10 ** 6)
    f, i = arr[0], 0
    count = 0
    for j in range(queries[i][0], queries[i][1] + 1):
        if not freqArr[arr[j]]:
            count += 1
        freqArr[arr[j]] += 1
    queries[0].append(count)

    while True:
        j = i + 1
        for j in range(i + 1, i + f):
            count, freqArr = adding(queries[j - 1][1], queries[j][1], freqArr, arr, count)
            queries[j].append(count)

        if j == len(queries): break
        count, freqArr = removing(queries[j - 1], queries[j], freqArr, arr, count)
        queries[j].append(count)
        i = j
        f = freq[queries[i][0]]

    answer = [0] * len(queries)
    for i in queries:
        answer[i[2]] = i[3]
    return answer


def distinctElementUtil(arr, queries):
    freq = {}
    for i in range(len(queries)):
        queries[i].append(i)
        if queries[i][0] not in freq:
            freq[queries[i][0]] = 1
        else:
            freq[queries[i][0]] += 1

    queries.sort()

    i = 0
    while i < len(queries):
        f = freq[queries[i][0]]
        queries[i:i + f] = sorted(queries[i:i + f], key=lambda a: a[1])
        i += f

    return mo(arr, queries, freq)


print(distinctElementUtil([1, 1, 2, 1, 3, 4, 5, 2, 8], [[2, 4], [1, 3], [0, 4]]))
