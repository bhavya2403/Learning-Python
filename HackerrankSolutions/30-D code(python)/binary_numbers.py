n = int(input())

bi = str(bin(n)[2:])
maximum = 0
for i in range(len(bi)-1):
    if bi[i] == '1':
        count = 1
        for j in range(i+1, len(bi)):
            if bi[j] == '1':
                count += 1
            else:
                if count > maximum:
                    maximum = count
                break

            if j == len(bi)-1:
                if count > maximum:
                    maximum = count
                    break

print(maximum)
