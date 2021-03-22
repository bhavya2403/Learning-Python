def binSearch(i, n, pile):
    lo, hi = 0, n - 1
    if n==1:
        return -1
    while lo < hi:
        if pile[lo + 1] > i:
            return lo
        if pile[hi - 1] < i:
            return hi-1
        mid_idx = (lo + hi) // 2
        mid = pile[mid_idx]
        if pile[mid_idx + 1] > i:
            return mid_idx
        if mid > i:
            hi = mid_idx - 1

        elif mid == i:
            return mid_idx - 1
        else:
            lo = mid_idx + 1


def longestSubsequence(arr, n): # O(nlog(n))
    pile = [arr[0]]
    count = 1
    for i in arr[1:]:
        if i > pile[count - 1]:
            pile.append(i)
            count += 1
        elif i == pile[count-1]:
            continue
        else:
            if i < pile[0]:
                j = -1
            else:
                j = binSearch(i, count, pile)  # returns the index pile[j] < i < pile[j+1]

            pile[j + 1] = i
    return count

def longestIncSubsequence(arr):
    n = len(arr)
    aux = [1] * n

    for i in range(1, n):
        for j in range(i):
            aux[i] = max(aux[i], aux[j])
            if arr[j] < arr[i] and aux[i] < aux[j]+1:
                aux[i] = aux[j]+1

    return aux[n-1]

print(longestIncSubsequence([10, 22, 9, 33, 21, 50, 41, 60] ))