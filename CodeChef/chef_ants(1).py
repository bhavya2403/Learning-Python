for _ in range(int(input())):
    arr = []
    max_dis_from_o = 0
    for m in range(int(input())):
        arr1 = list(map(int, input().split()))
        left_dist = min(arr1[1:])
        max_dist_in_line = max(-left_dist, max(arr1[1:]))
        if max_dist_in_line > max_dis_from_o:
            max_dis_from_o = max_dist_in_line

        arr2 = []
        for ele in arr1[1:]:
            arr2.append([ele, -1 if ele<0 else 1])
        arr.append(arr2)

    col_count = 0
    while True:
        zero_arr = []
        for i in range(len(arr)):
            size = len(arr[i])
            for j in range(size-1):
                num = arr[i][j][0]
                found = False
                if num > max_dis_from_o or num < -max_dis_from_o:
                    continue
                else:
                    found = True
                    if num == 0:
                        zero_arr.append([i, j])

                    if num == arr[i][j+1][0]:
                        arr[i][j][1], arr[i][j+1][1] = arr[i][j+1][1], arr[i][j][1]
                        col_count += 1

            num = arr[i][size-1][0]
            if num == 0:
                zero_arr.append([i, size-1])

        if len(zero_arr)>1:
            col_count += 1
            for k in zero_arr:
                [i, j] = k
                arr[i][j][1] = -1 if arr[i][j][1]==1 else 1

        if not found:
            break

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                arr[i][j][0] += 0.5 if arr[i][j][1]==-1 else -0.5

    print(col_count)