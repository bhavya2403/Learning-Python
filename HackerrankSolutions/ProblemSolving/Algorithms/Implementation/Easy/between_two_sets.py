def getTotalX(a, b):
    nums = [i for i in range(1, 101)]
    count = 0
    for num in nums:
        if all(num % i == 0 for i in a) and all(i % num == 0 for i in b):
            count += 1

    return count
