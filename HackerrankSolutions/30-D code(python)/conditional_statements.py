N = int(input())

if int(N) == 2 or int(N) == 4 :
    print('Not Weird')
elif int(N) % 2 == 0 and N > 20:
    print('Not Weird')
else:
    print('Weird')