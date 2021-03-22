import math

for i in range(int(input())):
    arr = input().split()
    n = int(arr[0])
    d = int(arr[1])
    at_risk = 0
    not_risky = 0
    people = input().split()
    for age in people:
        if int(age) >= 80 or int(age) <= 9:
            at_risk += 1
        else:
            not_risky += 1

    print(math.ceil(at_risk / d) + math.ceil((n - at_risk) / d))
