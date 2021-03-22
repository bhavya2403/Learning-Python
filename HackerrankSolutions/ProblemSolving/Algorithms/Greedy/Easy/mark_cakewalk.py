def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    n = len(calorie)
    tot = 0
    for i in range(n):
        tot += (2**i)*calorie[i]
    return tot