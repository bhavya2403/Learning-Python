inp = int(input())
d = {}

for i in range(inp):
    s = input().split()
    d[s[0]] = s[1]

while True:
    try:
        name = input()
        if name in d:
            print(name + '=' + d[name])
        else:
            print('Not found')
    except:
        break
