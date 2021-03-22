from random import random

square = 100000
for  _ in range(10):
    inside_cir = 0
    for i in range(square):
        x = random()
        y = random()
        if (x**2 + y**2) < 1:
            inside_cir += 1

    print(4*inside_cir/square)
