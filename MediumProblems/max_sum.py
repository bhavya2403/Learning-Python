# https://www.youtube.com/watch?v=8EhxxkHzGew

def maxSum(a, b):
    intersection = set(a) & set(b)
    max_sum = sum(intersection)
    i, j = 0, 0
    sumA, sumB = -1, -1
    while sumA or sumB:
        sumA, sumB = 0, 0
        while i < len(a):
            if a[i] in intersection:
                i += 1
                break
            sumA += a[i]
            i += 1
        while j < len(b):
            if b[j] in intersection:
                j += 1
                break
            sumB += b[j]
            j += 1
        max_sum += max(sumB, sumA)
    return max_sum


print(maxSum([1,3,5,8,10,12,14], [2,5,6,7,8,11,13,14,16,17]))