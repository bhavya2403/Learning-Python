arr = input().split()

if int(arr[0]) % 5 != 0 or (int(arr[0])+0.5 > float(arr[1])):
    print(arr[1])
else:
    print(float(arr[1])-0.5-int(arr[0]))