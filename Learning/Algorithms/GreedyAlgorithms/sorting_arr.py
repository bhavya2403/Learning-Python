def sortingArr(n, arr):
    sortA = sorted(arr)
    if n%2:
        if arr[n//2] == sortA[n//2]:
            for i in range(n//2):
                if (arr[i]==sortA[i] and arr[n-i-1]==sortA[n-i-1]) or (arr[i]==sortA[n-i-1] and arr[n-i-1]==sortA[i]):
                    continue
                return False
            return True
        return False
    if arr[n//2] == sortA[n//2] and arr[n//2-1]==sortA[n//2-1]:
        for i in range(n//2-1):
            if (arr[i] == sortA[i] and arr[n - i - 1] == sortA[n - i - 1]) or (
                    arr[i] == sortA[n - i - 1] and arr[n - i - 1] == sortA[i]):
                continue
            return False
        return True
    return False

print(sortingArr(7, [1, 6, 3, 4, 5, 7, 2]))