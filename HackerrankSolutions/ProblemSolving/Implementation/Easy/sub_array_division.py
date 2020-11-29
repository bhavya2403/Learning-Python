def birthday(s, d, m):
    index = 0
    summation = 0
    ways = 0
    while index < len(s) - m + 1:
        count = index
        for i in range(m):
            summation += s[count]
            count += 1
        if summation == d:
            ways += 1
        summation = 0
        index += 1

    return ways


print(birthday([1, 2, 1, 3, 2], 3, 2))
