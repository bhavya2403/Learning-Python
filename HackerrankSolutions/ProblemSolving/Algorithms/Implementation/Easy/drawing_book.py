def pageCount(n, p):
    flips = 0
    pageno = 1
    while p > pageno:
        pageno += 2
        flips += 1

    flips1 = 0
    pageno1 = n
    # if we don't use if statement here then let's say n=5 and p=4 it will give us output 1
    if pageno1 % 2 == 1:
        pageno1 -= 1
    while pageno1 > p:
        pageno1 -= 2
        flips1 += 1

    print(flips)
    print(flips1)

    return min(flips, flips1)


print(pageCount(6, 4))
