def fine(d1, m1, y1, d2, m2, y2):
    if y1 == y2 and m1 == m2:
        if d2 >= d1:
            return 0
        else:
            return 15 * (d1 - d2)
    elif y1 == y2:
        if m2 > m1:
            return 0
        else:
            return 500 * (m1 - m2)
    else:
        if y2 > y1:
            return 0
        else:
            return 10000
