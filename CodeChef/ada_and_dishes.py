def adaDishes(dishes):
    exp_min = sum(dishes) // 2
    while True:
        count = 0
        i = 0
        while i < len(dishes)-1:
            j = 0
            while j < len(dishes):
                if i + j == exp_min:
                    dishes[i] = 0
                    dishes[j] = 0
                    count += 1
