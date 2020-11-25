print(3 ** 5)


def raise_to_power(base_num, power_num):
    result = 1
    for bhavya in range(power_num):
        result = result * base_num
    return result


print(raise_to_power(int(input("Enter base number: ")), int(input("Enter power number: "))))
