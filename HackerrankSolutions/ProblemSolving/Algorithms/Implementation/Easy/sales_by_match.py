def sockMerchant(n, ary):
    count = 0
    count1 = 0
    for i in ary:
        if ary.count(i) >= 2:
            if ary.count(i) % 2 == 0:
                count += 0.5
            else:
                c = ary.count(i)
                count1 += (c-1)/(2*c)

    return int(round(count+count1))
