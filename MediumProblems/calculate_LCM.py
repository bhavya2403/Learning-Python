def lcm(n1, n2, n3):
    higher = max(n1, n2)
    while True:
        if higher % n1 == 0 and higher % n2 == 0 and higher % n3 == 0:
            print('lcm is', higher)
            break
        else:
            higher += max(n1, n2)


print(lcm(11, 12, 13))


def LCM(*numbers):
    ary = []
    for number in numbers:
        ary.append(number)
    maximum = max(numbers)
    num = maximum
    while True:
        if all(num % i == 0 for i in ary):
            print('lcm is ', num)
            break
        else:
            num += maximum


print(LCM(24, 36, 60))
