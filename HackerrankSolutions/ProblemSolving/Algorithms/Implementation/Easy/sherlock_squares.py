import math


def squares(a, b):
    count = 0
    j = 0
    found = False
    for i in range(a, b+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            j = math.sqrt(i) + 1
            count += 1
            found = True
            break
    if not found:
        return 0
    while True:
        if j ** 2 > b:
            break
        else:
            count += 1
        j += 1

    return count


print(squares(17, 24))
