def solve():
    adjList = {}
    for key in street:
        start, end, L = street[key]
        end = int(end)
        if end not in adjList:
            adjList[end] = [1, key]
        else:
            adjList[end][0] += 1
            adjList[end].append(key)

    streetsUsed = set()
    for path in carPaths:
        streetsUsed = streetsUsed.union(set(path[1:]))

    output.write(str(totIntersection) + '\n')
    for inter in adjList:
        count = 0
        notUsed = set()
        for i in range(1, adjList[inter][0] + 1):
            if adjList[inter][i] not in streetsUsed:
                count += 1
                notUsed.add(adjList[inter][i])

        output.write(str(inter) + '\n')
        if not adjList[inter][0]-count:
            output.write(str(1) + '\n')
            output.write(str(adjList[inter][1]) + ' ' + str(1) + '\n')
        else:
            output.write(str(adjList[inter][0]-count) + '\n')
            for i in range(1, adjList[inter][0]+1):
                if adjList[inter][i] not in notUsed:
                    output.write(str(adjList[inter][i]) + ' ' + str(1) + '\n')


input = open("f.txt", "r")
SimulationTime, totIntersection, totStreets, totCars, bonusPoints = map(int, input.readline().split())

street = {}
for _ in range(totStreets):
    start, end, streetName, L = input.readline().split()
    street[streetName] = (start, end, L)

carPaths = []
for _ in range(totCars):
    path = list(input.readline().split())
    carPaths.append(path)
carPaths.sort(key=lambda a:int(a[0]))

input.close()

output = open("fOutput", "w")
solve()
output.close()