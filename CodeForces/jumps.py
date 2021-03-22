from math import sqrt

for _ in range(int(input())):
    x = int(input())
    jumps = (sqrt(1+8*x)-1)/2
    if jumps == int(jumps):
        print(int(jumps))
    else:
        jumps = int(jumps)+1
        if x== (jumps*(jumps+1)/2)-1:
            print(jumps+1)
        else:
            print(jumps)
