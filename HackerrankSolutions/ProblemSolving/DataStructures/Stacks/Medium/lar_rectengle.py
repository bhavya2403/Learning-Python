def largestRectangle(h):
    size = len(h)
    largest = size
    maximum = size * max(h)
    for i in range(1, size - 1):
        area = h[i]
        j, k = i - 1, i + 1
        while h[i] > 1:
            found1, found2 = False, False
            if j >= 0:
                if h[j] >= h[i]:
                    area += h[i]
                    j -= 1
                    found1 = True
            if k < size:
                if h[k] >= h[i]:
                    area += h[i]
                    k += 1
                    found2 = True

            if not found1 and not found2:
                break
        if area == maximum:
            return area
        if area > largest:
            largest = area
    return largest

print(largestRectangle([1,3,5,9,11]))