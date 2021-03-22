def solve(a, b, lo1, hi1, lo2, hi2):
    if lo2>=hi2:
        return lo1
    midIdx = lo1 + (hi1-lo1+1)//2
    if not (hi1-lo1+1)%2:
        midIdx -= 1

    if a[midIdx] == b[midIdx]:
        return solve(a, b, midIdx+1, hi1, midIdx+1, hi2)
    elif lo1==midIdx:
        return midIdx
    return solve(a, b, lo1, midIdx, lo2, midIdx)

def findExtra(a, b, n):
    return solve(a, b, 0, n-1, 0, n-2)


print(findExtra([2,4,6,8, 9, 10, 12], [2,4,6, 8, 9, 10], 7))