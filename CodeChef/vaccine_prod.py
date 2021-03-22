import math

arr = input().split()
d1 = int(arr[0])
v1 = int(arr[1])
d2 = int(arr[2])
v2 = int(arr[3])
p = int(arr[4])
v = v1 + v2

# 3 2 3 3 14
if d1 == d2:
    v = v1 + v2
    print(d1 + math.ceil(p/v) - 1 if v<p else d1)

# 3 2 5 5 19 more 15, v is 7, wer at day 5
elif d1 < d2:
    vac_produced = (d2-d1) * v1
    if vac_produced < p:
        p -= vac_produced
        print(d2 + math.ceil(p/v) - 1)
    else:
        print(d1 + math.ceil(p/v1) -1)

else:
    vac_produced = (d1-d2) * v2
    if vac_produced < p:
        p -= vac_produced
        print(d1 + math.ceil(p/v) - 1)
    else:
        print(d2 + math.ceil(p/v2) -1)