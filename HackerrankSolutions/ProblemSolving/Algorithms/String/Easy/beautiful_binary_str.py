def beautifulBinaryString(b):
    count = 0
    idx = 0
    while idx < len(b) - 2:
        if int(b[idx]) == int(b[idx + 2]) == 0 and int(b[idx + 1]) == 1:
            count += 1
            idx += 3
        else:
            idx += 1

    return count