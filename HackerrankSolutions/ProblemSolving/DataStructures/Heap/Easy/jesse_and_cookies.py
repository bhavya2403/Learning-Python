from heapq import heapify, heappop, heappush

def cookies(k, A):
    count = 0
    heapify(A)
    try:
        while A[0] < k:
            mini = heappop(A)
            last_mini = heappop(A)
            heappush(A, mini + (last_mini*2))
            count += 1
        return count
    except:
        return -1