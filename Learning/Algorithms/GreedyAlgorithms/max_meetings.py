def maximumMeetings(n, start, end):
    if n == 1:
        return 1

    se = [(start[i], end[i]) for i in range(n)]
    se.sort(key=lambda a: a[1])
    totMeets = 1
    i, j = 0, 1
    while j < n:
        if se[j][0] > se[i][1]:
            i = j
            totMeets += 1
        else:
            j += 1
    return totMeets

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(maximumMeetings(n, start, end))

