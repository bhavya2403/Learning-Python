def countTriplets(arr, r):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    count = 0
    if r == 1:
        for key in d:
            count += d[key] * (d[key] - 1) * (d[key] - 2) / 6
        return int(count)
    else:
        for key in d:
            try:
                count += d[key] * d[key * r] * d[key * r * r]
            except:
                continue
        return count