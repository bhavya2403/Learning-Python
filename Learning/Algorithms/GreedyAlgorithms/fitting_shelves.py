def fittingShelves(w, m, n):
    M, N, printSwapped = m, n, False
    m, n = max(m, n), min(m, n)
    if m==N:
        printSwapped = True
    maxM, maxN = w//m, w//n
    a, b = maxM, maxN
    printA, printB = a, b
    minSLeft = w
    while a:
        b = (w-(m*a))//n
        sLeft = w-(m*a)-(n*b)
        if sLeft < minSLeft:
            printB = b
            printA = a
            minSLeft = sLeft
        if not minSLeft:
            break
        a -= 1

    if not printSwapped:
        print(printA, printB, minSLeft)
    else:
        print(printB, printA, minSLeft)

fittingShelves(24, 3, 5)
fittingShelves(29, 3, 9)
fittingShelves(24, 4, 7)