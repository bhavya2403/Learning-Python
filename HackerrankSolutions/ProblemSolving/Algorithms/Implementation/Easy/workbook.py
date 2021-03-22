def workbook(n, k, arr):
    # n - num of chapters(len(arr))
    # k - max-prob on page can contain
    pageNo = 1
    speProbs = 0
    for idx in range(n):
        if k >= arr[idx]:
            if pageNo in range(arr[idx] + 1):
                speProbs += 1
            pageNo += 1
        else:
            probNo = 1
            while True:
                if pageNo in range(probNo, probNo + k if arr[idx] > probNo + k else arr[idx] + 1):
                    speProbs += 1
                if probNo > arr[idx]:
                    break
                probNo += k
                pageNo += 1

    return speProbs


print(workbook(5, 3, [4, 2, 6, 1, 10]))
