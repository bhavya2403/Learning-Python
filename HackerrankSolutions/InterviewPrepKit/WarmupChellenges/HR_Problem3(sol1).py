# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumping_clouds(c):
    print(c)
    index = 0
    while True:
        if index + 2 < len(c):
            for i in c:
                if c[index] == 0 and c[index + 1] == 0 and c[index + 2] == 0:
                    c[index + 1] = 1
            index += 1
        elif index + 2 == len(c):
            break
    print(c)
    count = 0
    for i in c:
        if i == 0:
            count += 1

    return count - 1


print(jumping_clouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]))
