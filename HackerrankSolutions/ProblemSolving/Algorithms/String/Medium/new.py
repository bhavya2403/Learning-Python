def maxPal(s, l, r):
    s = list(s[l-1:r].rstrip())
    max_len = 0
    mid = len(s)//2
    lo = 0
    hi = len(s)-1
    while max_len < mid:
        i = mid-1
        j = mid+1
