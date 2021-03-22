for _ in range(int(input())):
    sample = "party"
    s = input()
    n = len(s)
    arr = [i for i in s]
    for i in range(n-4):
        found = False
        for j in range(i, i+5):
            if arr[j] != sample[j-i]:
                break
            else:
                if j == i+4:
                    found = True

        if found:
            arr[i+2] = 'w'
            arr[i+3] = 'r'
            arr[i+4] = 'i'

    for i in arr:
        print(i, end='')
    print()
