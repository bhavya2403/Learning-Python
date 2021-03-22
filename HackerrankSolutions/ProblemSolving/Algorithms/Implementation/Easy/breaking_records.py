def breakingRecords(scores):
    maximum = scores[0]
    minimum = scores[0]
    countMAX = 0
    countMIN = 0
    for i in scores:
        if i > maximum:
            countMAX += 1
            maximum = i
        elif i < minimum:
            countMIN += 1
            minimum = i

    return [countMAX, countMIN]


print(breakingRecords(
    [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
