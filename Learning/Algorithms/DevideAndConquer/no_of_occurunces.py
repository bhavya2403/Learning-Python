def findLast(l, h, arr, x):
    if arr[h]==x:
        return h
    if l+1==h:
        return l
    if arr[l + 1] != x:
        return l
    while True:
        last = (l + h) // 2
        if arr[last] > x:
            if arr[last - 1] == x:
                return last-1
            h = last - 1
        else:
            l = last + 1

def numberOccurrences(arr, n, x):
    l, h = 0, n-1
    lastLessThan = n-1
    if arr[n-1] < x or arr[0] > x:
        return 0
    while l <= h:
        first = (l+h)//2
        if not first:
            if arr[first]==x:
                return findLast(0, lastLessThan, arr, x)+1
        if arr[first] < x:
            if arr[first+1] == x:
                return findLast(first, lastLessThan, arr, x)-first
            l = first +1
        elif arr[first] > x:
            lastLessThan = first
            h = first-1
        else:
            h = first-1
    return 0

print(numberOccurrences([10,10], 2, 10))