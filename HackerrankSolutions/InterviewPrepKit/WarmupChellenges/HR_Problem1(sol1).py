# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(ary):
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


print(sockMerchant([4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]))
