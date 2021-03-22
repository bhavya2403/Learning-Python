def dynamicArray(n, queries):
    result = []
    matrix = [[] for _ in range(n)]
    lastAnswer = 0
    for query in queries:
        x = query[1]
        y = query[2]
        idx = (x ^ lastAnswer) % n
        if query[0] == 1:
            matrix[idx].append(y)
        elif query[0] == 2:
            idy = y % len(matrix[idx])
            lastAnswer = matrix[idx][idy]
            result.append(lastAnswer)
    return result


print(dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]))
