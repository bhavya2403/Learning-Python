def makeAnagram(a, b):
    ara = []
    for char in a:
        ara.append(char)
    arb = []
    for char in b:
        arb.append(char)

    indeA = 0
    for char in ara:
        indeB = 0
        for charb in arb:
            if char == charb:
                ara[indeA] = 0
                arb[indeB] = 0
            indeB += 1
            break
        indeA += 1

    indB = 0
    for charb in arb:
        indA = 0
        for char in ara:
            if char == charb:
                ara[indA] = 0
                arb[indB] = 0
            indA += 1
            break
        indB += 1


    count = 0
    for char in ara:
        if char != 0:
            count += 1

    countb = 0
    for char in arb:
        if char != 0:
            countb += 1

    print(ara)
    print(arb)
    return count + countb


print(makeAnagram('abc', 'bcdma'))
