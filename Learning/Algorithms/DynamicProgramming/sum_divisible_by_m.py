from math import ceil

def solve(num, setArr):
    global possible
    flag = False

    if num in setArr:
        flag = True
    else:
        for i in setArr:
            if i > num:
                break
            if possible[num-i]!=-1:
                if possible[num-i]:
                    flag = True
                break
            elif solve(num-i, setArr-{i}):
                flag = True
                break

    if flag:
        possible[num] = True
    else:
        possible[num] = False

    return flag


def sumOfSubset(m, arr):
    global possible

    arr.sort()
    possible = [-1] * (sum(arr)+1)
    l, r = ceil(min(arr)/m), sum(arr)//m

    for num in range(l, r+1):
        if solve(m*num, set(arr)):
            return True

    return False

print(sumOfSubset(1, [3,1,7,5]))