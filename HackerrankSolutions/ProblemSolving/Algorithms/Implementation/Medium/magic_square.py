import math


def magicSquare(s):
    s1 = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    s2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    s3 = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    s4 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    s5 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
    s6 = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    s7 = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    s8 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    cost1 = cost2 = cost3 = cost4 = cost5 = cost6 = cost7 = cost8 = 0
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if s[i][j] != s1[i][j]:
                cost1 += int(math.fabs(s[i][j] - s1[i][j]))
            if s[i][j] != s2[i][j]:
                cost2 += int(math.fabs(s[i][j] - s2[i][j]))
            if s[i][j] != s3[i][j]:
                cost3 += int(math.fabs(s[i][j] - s3[i][j]))
            if s[i][j] != s4[i][j]:
                cost4 += int(math.fabs(s[i][j] - s4[i][j]))
            if s[i][j] != s5[i][j]:
                cost5 += int(math.fabs(s[i][j] - s5[i][j]))
            if s[i][j] != s6[i][j]:
                cost6 += int(math.fabs(s[i][j] - s6[i][j]))
            if s[i][j] != s7[i][j]:
                cost7 += int(math.fabs(s[i][j] - s7[i][j]))
            if s[i][j] != s8[i][j]:
                cost8 += int(math.fabs(s[i][j] - s8[i][j]))
            j += 1
        i += 1

    return min(cost1, cost2, cost3, cost4, cost5, cost6, cost7, cost8)
