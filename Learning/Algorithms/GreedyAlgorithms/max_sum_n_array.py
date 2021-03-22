#  maximize sum of i where i is element from each array
#  i should be greater than i taken from last array

def maxSum(matrix):
    n = len(matrix)
    maxSum = max(matrix[n-1])
    lastEle = maxSum
    n -= 2
    while n>=0:
        ele = 0
        for i in matrix[n]:
            if i>ele and i < lastEle:
                ele = i
        if not ele:
            return 0

        maxSum += ele
        lastEle = ele
        n -= 1

    return maxSum

print(maxSum([[1, 7, 3, 4],
                   [4, 2, 5, 1],
                   [9, 5, 1, 8]]))