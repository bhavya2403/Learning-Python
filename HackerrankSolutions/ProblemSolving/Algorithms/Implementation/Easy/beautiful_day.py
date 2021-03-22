import math


def beautifulDays(i, j, k):

    count = 0
    for num in range(i, j+1):
        k1 = str(num)
        k2 = k1[::-1]
        k3 = math.fabs(int(k2)-int(k1))
        if k3 % k == 0:
            count += 1

    return count


print(beautifulDays(20,23,6))
