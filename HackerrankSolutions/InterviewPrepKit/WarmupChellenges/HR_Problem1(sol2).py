# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ary):
    findevendupl1 = []
    count = 0
    for i in ary:
        if ary.count(i) % 2 == 0:
            findevendupl1.append(i)
        count += 1
    a = set(findevendupl1)
    uniques1 = []
    for i in ary:
        if i not in uniques1:
            uniques1.append(i)
    b = set(uniques1)
    list1 = list(b - a)
    return (n-(len(list1)))/2


print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
