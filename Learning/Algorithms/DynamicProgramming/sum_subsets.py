def solve(s, n):
    global lookup

    flag = False
    if n in s:
        flag = True
    else:
        for ele in s:
            if ele < n:
                if lookup[n-ele]:
                    flag = True
                    break
                elif solve(s-{ele}, n-ele):
                    flag = True
                    break

    if flag:
        lookup[n] = True
    return flag


def sumSubsets(arr, summation):
    global lookup
    lookup = [0] * (summation+1)
    s = set(arr)
    return solve(s, summation)


print(sumSubsets([3, 34, 4, 12, 5, 2], 9))