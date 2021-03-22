def miniMaxSum(arr):
    ar1 = []
    ar1.append(sum(i for i in arr) - arr[0])
    ar1.append(sum(i for i in arr) - arr[1])
    ar1.append(sum(i for i in arr) - arr[2])
    ar1.append(sum(i for i in arr) - arr[3])
    ar1.append(sum(i for i in arr) - arr[4])

    print(str(min(ar1)) + " " + str(max(ar1)))

miniMaxSum([1,3,5,7,9])