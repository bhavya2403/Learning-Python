s = ''
undo = []
for _ in range(int(input())):
    arr = input().split()
    n = arr[0]
    if n=='1':
        undo.append(s)
        s += arr[1]
    elif n=='2':
        undo.append(s)
        s = s[:len(s)-int(arr[1])]
    elif n=='3':
        print(s[int(arr[1])-1])
    else:
        s = undo.pop()
