def beautifulTriplets(d, arr):
    count = 0
    for i in range(len(arr)-2):
        if arr[i]+d in arr and arr[i]+(2*d) in arr:
            count += 1
    return count