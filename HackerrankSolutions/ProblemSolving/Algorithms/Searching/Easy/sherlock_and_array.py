def balancedSums(arr):
    sumARR = sum(arr)
    sumL = 0
    for idx in range(len(arr)):
        sumL += 0 if idx==0 else arr[idx-1]
        sumR = sumARR - sumL - arr[idx]
        if sumL == sumR:
            return 'YES'
    return 'NO'