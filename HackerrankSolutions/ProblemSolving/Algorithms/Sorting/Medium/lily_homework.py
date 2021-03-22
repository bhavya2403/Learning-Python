# 7 15 12 3 , 3 7 12 15
# d = {15:1, 7:0, 12:2, 3:3}

def lilysHomework(arr):
    arrD = arr.copy()
    sor_arr = sorted(arr)
    rev_arr = sor_arr.copy()
    rev_arr.reverse()
    d = {}
    for i, ele in enumerate(arr):
        d[ele] = i
    dD = d.copy()
    swapsA = swapsD = 0
    for i, ele in enumerate(sor_arr):
        if ele == arr[i]:
            continue
        idx = d[ele]
        d[ele], d[arr[i]] = i, idx
        arr[i], arr[idx] = arr[idx], arr[i]
        swapsA += 1
    for i, ele in enumerate(rev_arr):
        if ele == arrD[i]:
            continue
        idx = dD[ele]
        dD[ele], dD[arrD[i]] = i, idx
        arrD[i], arrD[idx] = arrD[idx], arrD[i]
        swapsD += 1

    return min(swapsA, swapsD)

# print(lilysHomework([3,4,2,5,1]))
n = int(input())
arr = list(map(int, input().split()))
print(lilysHomework(arr))