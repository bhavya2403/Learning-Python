# l = 54, rootl = n+h (6*9, x=1, )
# area = (n-x)(n+1+x) ,  n >2h + 1
from math import sqrt

def encryption(s):
    length = sum(len(i) for i in s.split())
    cols = int(sqrt(length))
    cols = cols if sqrt(length) == cols else cols + 1
    col = 0
    arr = ['']*cols
    for i in s:
        if i == ' ':
            continue
        else:
            if col == cols-1:
                arr[col] += i
                col = 0
            else:
                arr[col] += i
                col += 1
    result = ''
    for i in arr:
        result += i + ' '
    return result


result = encryption('if man was meant to stay on the ground god would have given us roots')

print(result)
# ifmanwas
# meanttos
# tayonthe
# groundgo
# dwouldha
# vegivenu
# sroots