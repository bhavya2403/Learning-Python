n = int(input())
for i in range(10, 0, -1):
    if not n%i:
        print(i)
        break