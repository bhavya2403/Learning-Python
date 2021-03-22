n = int(input())

lengths = {}

for _ in range(n):
    number = input()
    length = len(number)
    if length not in lengths:
        lengths[length] = []

    lengths[length].append(number)

for key in sorted(lengths):
    for value in sorted(lengths[key]):
        print(value)

