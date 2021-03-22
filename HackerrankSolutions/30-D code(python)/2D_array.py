arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))


def hourglassSum(matrix):
    maximum = -100
    i = 0
    while i < 6:
        j = 0
        while j < 6:
            if i < len(matrix) - 2 and j < len(matrix) - 2:
                summ = matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 1] + matrix[i + 2][j] + \
                        matrix[i + 2][j + 1] + matrix[i + 2][j + 2]
                if summ > maximum:
                    maximum = summ
            j += 1
        i += 1

    return maximum


print(hourglassSum(arr))
