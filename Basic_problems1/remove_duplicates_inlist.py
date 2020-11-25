numbers = [1,2,1,2,1,3,2]

for number in numbers:
    print(numbers.count(number))
    if numbers.count(number) >= 2:
        numbers.remove(number)
print(numbers)

numbers1 = [1, 2, 5, 10, 6, 5, 5, 10]
uniques = []
for number in numbers1:
    if number not in uniques:
        uniques.append(number)
print(uniques)

