# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def countingValleys(path):
    ar = [0]
    for char in path:
        if char == "D":
            ar.append(int(ar[len(ar) - 1]) - 1)
        else:
            ar.append(int(ar[len(ar) - 1]) + 1)
    print(ar)

    index = 0
    count = 0
    while True:
        if index + 1 < len(ar):
            if ar[index] == 0 and ar[index + 1] == -1:
                count += 1
        elif index + 1 == len(ar):
            break
        index += 1

    return count

print(countingValleys("DDUUDDUDUUUD"))