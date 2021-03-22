def steadyGene(size, gene):
    high = {}
    d = {}
    minimum = 0
    for i in gene:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
            if i in high:
                high[i] += 1
                minimum += 1
            elif d[i] > size/4:
                high[i] = 1
                minimum += 1

    for count in range(minimum, size+1):
        for i in range(size-count+1):
            d1 = high.copy()
            for j in range(i, count+i):
                if gene[j] in d1:
                    if d1[gene[j]]==1:
                        d1.__delitem__(gene[j])
                    else:
                        d1[gene[j]] -= 1
            if not d1:
                return count
        print(count)

# n = int(input())
# gene = input()
# print(steadyGene(n, gene))
print(steadyGene(8, 'GAAATAAA'))