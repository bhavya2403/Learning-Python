import math

for i in range(int(input())):
    notP = False
    num = int(input())
    if num == 1:
        print("Not prime")
    elif num == 2:
        print("Prime")
    else:
        for j in range(2, math.ceil(math.sqrt(num) + 1)):
            if num % j == 0:
                notP = True
                print("Not prime")
                print(j)
                break
        if not notP:
            print("Prime")

