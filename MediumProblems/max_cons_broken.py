# https://www.youtube.com/watch?v=rw4s4M3hFfs

def binSearch(n, arr):
    lo, hi = 0, n-1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid]:
            if not arr[mid + 1]:
                return mid + 1
            lo = mid + 1
        elif not arr[mid]:
            if arr[mid - 1]:
                return mid
            hi = mid - 1

    return 0 if not arr[0] else n


def maxConsDec(arr):
    count, maxSeq, consDec, per, lastPer = [], 0, 1, 0, 0
    for i in arr:
        t = binSearch(len(i), i)
        curr = t / len(i)
        count.append(curr)
        if not per:
            per = curr
        elif not lastPer:
            lastPer, per = per, curr
        else:
            lastPer, per = per, curr
            if lastPer > per:
                consDec += 1
            else:
                consDec = 1

            if consDec > maxSeq:
                maxSeq = consDec

    return maxSeq


arr = [
    [True, True, True, False, False],
    [True, True, True, True, False],
    [True, True, True, True, True, True, False, False, False],
    [True, False, False, False, False, False],
    [True, True, True, True, True, True, True, True, True, True, True, True, False],
    [True, False],
    [True, True, True, True, False, False]
]
print(maxConsDec(arr))
