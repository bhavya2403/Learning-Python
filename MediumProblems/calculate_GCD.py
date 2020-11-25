def gcd(*numbers):
    # finding divisors and storing in array
    array = []
    for number in numbers:
        for i in range(1, number + 1):
            if number % i == 0:
                array.append(i)
    print(array)

    # finding common divisors in all numbers
    array1 = []
    for j in array:
        if array.count(j) == len(numbers):
            array1.append(j)
    print(array1)

    # finding maximum divisor and that's the answer
    maximum = array1[0]
    for num in array1:
        if num >= maximum:
            maximum = num
    return maximum


print(gcd(24, 36, 60, 90))





