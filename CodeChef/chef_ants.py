def check_zeros(arr, col_count):
    zeros_arr = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j][0] == 0:
                zeros_arr.append([i, j])
    if len(zeros_arr)!=1 and len(zeros_arr)!=0:
        for k in zeros_arr:
            [i, j] = k
            arr[i][j][1] = -1 if arr[i][j][1]==1 else -1
        col_count += 1
    return arr, col_count


for _ in range(int(input())):
    arr = []
    max_dis_from_o = 0
    for m in range(int(input())):
        arr1 = list(map(int, input().split()))
        left_dist = min(arr1[1:])
        max_dist_in_line = max(-left_dist, max(arr1[1:]))
        if max_dist_in_line > max_dis_from_o:
            max_dis_from_o = max_dist_in_line
        arr.append(arr1[1:])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = [arr[i][j], -1 if arr[i][j]<0 else 1]

# everytime we need to loop through array twice
    col_count = 0
    while True:
        arr, col_count = check_zeros(arr, col_count)
        for i in range(len(arr)):
            for j in range(len(arr[i])-1):
                num = arr[i][j][0]
                found = False
                if num > max_dis_from_o or num < -max_dis_from_o:
                    continue
                else:
                    found = True
                    if num == arr[i][j+1][0]:
                        col_count += 1
                        arr[i][j][1], arr[i][j+1][1] = arr[i][j+1][1], arr[i][j][1]

                    arr[i][j][0] += 1/2 if arr[i][j][1]==-1 else -1/2
            if len(arr[i])!=1:
                arr[i][j+1][0] += 1 / 2 if arr[i][j+1][1] == -1 else -1 / 2
            else:
                arr[i][j][0] += 1 / 2 if arr[i][j][1] == -1 else -1 / 2
        if not found:
            break
    print(col_count)
