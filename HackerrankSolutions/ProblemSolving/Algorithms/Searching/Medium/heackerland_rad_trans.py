def hackerlandRadioTransmitters(x, k):
    if len(x)==1:
        return 1
    if len(x)==2:
        return 1 if x[1]-x[0] <=k else 2
    x.sort()
    n = len(x)
    i = 0
    count = 0
    while i < n:
        right_range = x[i] + k
        while i < n and x[i] <= right_range:
            i += 1
        count += 1
        right_range = x[i-1] + k
        while i < n and x[i] <= right_range:
            i += 1

    return count


print(hackerlandRadioTransmitters([1,2,3,5,9], 1))
