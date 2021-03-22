from calculate_GCD import gcd

def lcm(numbers):
    GCD = gcd(numbers)
    LCM = GCD
    for i in numbers:
        LCM *= i/GCD

    return LCM

print(lcm([24, 36, 60]))
