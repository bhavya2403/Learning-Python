def makeAnagram(a, b):
    indeA = 0
    for char in a:
        indeB = 0
        for charb in b:
            if char == charb:
                a.replace(a[indeA], '')
                b.replace(b[indeB], '')
            indeB += 1
            break
        indeA += 1

    indB = 0
    for charb in b:
        indA = 0
        for char in a:
            if char == charb:
                a.replace(a[indA], '')
                b.replace(b[indB], '')
            indA += 1
            break
        indB += 1

    return len(a) + len(b)


print(makeAnagram('abc', 'bcdma'))
