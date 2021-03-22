boutput = open("bOutput", "r")
n = int(boutput.readline())
assigned = set()
broken = False
for _ in range(n):
    arr = list(map(int, boutput.readline().split()))
    for i in arr[1:]:
        if i in assigned:
            broken = True
            break
        assigned.add(i)

if broken:
    print(False)
else:
    print(True)