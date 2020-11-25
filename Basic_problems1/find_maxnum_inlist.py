numbers = [1, 2, 5, 10, 6, 5, 5, 10]

maximum = numbers[0]
for number in numbers:
    if number >= maximum:
        maximum = number
print(maximum)

for number in numbers:
    print('x' * number)
