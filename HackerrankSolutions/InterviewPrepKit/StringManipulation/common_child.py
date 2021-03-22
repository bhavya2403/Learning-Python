def commonChild(s1, s2):
    ar1 = [i for i in s1]
    ar2 = [i for i in s2]
    ar3 = []
    i = j = ind1 = ind2 = 0
    while True:
        count1 = 0
        found = False
        for ind1 in range(i, len(ar1)):
            for ind2 in range(j, len(ar2)):
                if ar1[ind1] == ar2[ind2] != 0:
                    ar1[ind1] = 0
                    ar2[ind2] = 0
                    count1 += 1
                    ind1 += 1
                    found = True
                    break
                ind2 += 1
            ind1 += 1

            if found:
                i = ind1
                j = ind2

        if ind1 == len(s1) and ind2 == len(s2)  and found:
            i = 0
            j = 0
        elif ind1 == len(s1)-1 and ind2 == len(s2)-1  and found:
            break

    count2 = 0
    i = j = ind1 = ind2 = 0
    for ind2 in range(j, len(s2)):
        found = False
        for ind1 in range(i, len(s1)):
            if s2[ind2] == s1[ind1]:
                count2 += 1
                found = True
                ind1 += 1
                break
            ind1 += 1
        ind2 += 1

        if found:
            i = ind1
            j = ind2
    print(count1)
    print(count2)

    return max(count1, count2)


print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))
