arry = []


def CheckPrime(numbertocheck):
    for i in range(2, numbertocheck):
        if numbertocheck % i == 0:
            arry.append("yes")
        else:
            arry.append("no")


CheckPrime(19)

if arry.count("yes") >= 1:
    print("It's not a prime number")
else:
    print("It's a prime number")



