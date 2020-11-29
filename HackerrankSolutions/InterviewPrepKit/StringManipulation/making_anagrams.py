def makeAnagram(a, b):
    ara = []
    for char in a:
        ara.append(char)
    arb = []
    for char in b:
        arb.append(char)

    count = 0
    for indA in range(len(ara)):
        for indB in range(len(arb)):
            if ara[indA] == arb[indB]:
                ara[indA] = 0
                arb[indB] = 0
                count += 2
                break

    print(ara)
    print(arb)
    return len(ara) + len(arb) - count


print(makeAnagram('abc', 'bcdma'))
