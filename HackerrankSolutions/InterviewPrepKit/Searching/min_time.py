def search_day(low, upp, d, goal):
    while True:
        mid_day = (low+upp) //2
        count = sum(d[machine]*(mid_day//machine) for machine in d)
        if count > goal:
            sum1 = sum(d[machine]*((mid_day-1)//machine) for machine in d)
            if  sum1<goal:
                return mid_day
            elif sum1 == goal:
                return mid_day
            else:
                upp = mid_day - 1
        elif count < goal:
            sum1 = sum(d[machine] * ((mid_day + 1) // machine) for machine in d)
            if sum1 > goal:
                return mid_day+1
            elif sum1 == goal:
                return mid_day + 1
            else:
                low = mid_day + 1
        else:
            return mid_day


def minTime(n, machines, goal):
    d = {}
    maximum = 0
    minimum = 1000000000
    for machine in machines:
        if machine > maximum:
            maximum = machine
        if machine < minimum:
            minimum = machine

        if machine not in d:
            d[machine] = 1
        else:
            d[machine] += 1

    upp_day = ((goal//n)) * maximum
    low_day = ((goal//n)) * minimum
    day = search_day(low_day, upp_day, d, goal)
    return day


# print(minTime(3, [4,5,6], 12))
n, goal = map(int, input().split())
machines = list(map(int, input().split()))
print(minTime(n, machines, goal))