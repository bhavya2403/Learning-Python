def countApplesAndOranges(s, t, a, b, apples, oranges):
    appcount = 0
    orcount = 0
    for apple in apples:
        apple += a
        if s <= apple <= t:
            appcount += 1
    for orange in oranges:
        orange += b
        if s <= orange <= t:
            orcount += 1

    print(appcount)
    print(orcount)