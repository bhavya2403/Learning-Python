
def left_rotation(arr, d):
    if d > len(arr):
        d = d - (len(arr)*(d % len(arr)))
    for i in range(0, d):
        arr.insert(len(arr), arr[0])
        del arr[0]
    return arr


print(left_rotation([1,2,3,4,5], 6))
