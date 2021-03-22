def organizingContainers(n, container):
    len_cont = [0] * n
    sum_types = [0] * n
    for i in range(n):
        for j in range(n):
            num = container[i][j]
            len_cont[i] += num
            sum_types[j] += num

    for i in range(n):
        swapped = False
        for j in range(i, n):
            if len_cont[i] == sum_types[j]:
                swapped = True
                sum_types[i], sum_types[j] = sum_types[j], sum_types[i]
                break

        if j == n-1 and not swapped:
            return 'Impossible'

    return 'Possible'

q = int(input())

for q_itr in range(q):
    n = int(input())

    container = []

    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))

    print(organizingContainers(n, container))

# why below code giving TLE: we don't need to check (No two balls of the same type are located in different containers.)

#               ANOTHER CODE WHICH IS CORRECT BUT GIVING TLE ERROR
# def organizingContainers(max_len_cont, sum_types, len_cont):
#     for i, ele in enumerate(sum_types):
#         if ele > max_len_cont:
#             return 'Impossible'
#
#         if ele in len_cont:
#             len_cont[ele] -= 1
#             sum_types[i] = 0
#         else:
#             j = ele + 1
#             while j <= max_len_cont:
#                 if j in len_cont:
#                     len_cont[j] -= 1
#                     if len_cont[j] == 0:
#                         len_cont.__delitem__(j)
#
#                     if ele - j not in len_cont:
#                         len_cont[ele-j] = 1
#                     else:
#                         len_cont[ele-j] += 1
#                 j += 1
#             if j==max_len_cont+1:
#                 return 'Impossible'
#
#     return 'Possible'
#
#
# q = int(input())
#
# for q_itr in range(q):
#     n = int(input())
#     sum_types = [0]*n
#     len_cont = {}
#     max_len_cont = 0
#
#     for _ in range(n):
#         arr = list(map(int, input().rstrip().split()))
#         summation = 0
#         for i, ele in enumerate(arr):
#             summation += ele
#             sum_types[i] += ele
#
#         if summation > max_len_cont:
#             max_len_cont = summation
#         if summation not in len_cont:
#             len_cont[summation] = 1
#         else:
#             len_cont[summation] += 1
#
#
#     print(organizingContainers(max_len_cont, sum_types, len_cont))
