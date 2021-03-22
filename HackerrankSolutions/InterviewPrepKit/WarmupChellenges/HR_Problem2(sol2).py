# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(steps, path):
    ar = [0]
    for char in path:
        if char == "D":
            ar.append(int(ar[len(ar)-1])-1)
        else:
            ar.append(int(ar[len(ar)-1])+1)
    print(ar)
    ar1 = []
    for i in ar:
        if i != 0:
            ar1.append(i)
    print(ar1)

    arIdx = 0
    ar1Idx = 0
    score = 0
    while arIdx < len(ar) and ar1Idx < len(ar1):
        if ar[arIdx] == 0 and ar1[ar1Idx] == -1:
            score += 1
        else:
            ar1Idx += 1
        arIdx += 1

    return score


print(countingValleys(12,"DDUUDDUDUUUD"))
