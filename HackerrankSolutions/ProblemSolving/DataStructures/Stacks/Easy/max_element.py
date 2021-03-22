stack = [0]
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        x = arr[1]
        stack.append(max(stack[-1], x))
    elif arr[0] == 2:
        stack.pop()
    else:
        print(stack[-1])
