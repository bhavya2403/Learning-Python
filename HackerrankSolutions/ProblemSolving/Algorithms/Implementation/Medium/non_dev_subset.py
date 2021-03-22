# [19,10,12,10,24,25,22]
# 1+3, 2+2
# (25)+(19), (10,10,22), (12,24)


def nonDivisibleSubset(k, s):
    d = {i: 0 for i in range(k)}
    for ele in set(s):
        d[ele%k] += 1

    count = 0
    for ele in d:
        if ele > k//2:
            break

        if ele == 0:
            if d[0] != 0:
                count += 1
            continue

        if k % 2 == 0 and ele == k/2:
            if d[ele] != 0:
                count += 1
            break

        count += max(d[ele], d[k-ele])

    return count

print(nonDivisibleSubset(3, [1,7,2,4]))

