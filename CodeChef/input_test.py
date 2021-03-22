arr = input().split()
n = int(arr[0])
k = int(arr[1])
count = 0

for num in range(n):
    if int(input()) % k == 0:
        count += 1

print(count)