def strangeCounter(t):
    if t == 1:
        return 3
    value = 3
    time = 3
    while time < t:
        tmp = time
        value *= 2
        time += value

    return value - (t - tmp) + 1