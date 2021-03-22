def absolutePermutation(n, k):
    if k == 0:
        return [i for i in range(1, n+1)]
    elif (n/k) % 2 != 0:
        return [-1]

    arr = [0] * n
    plus = True
    for i in range(1, n+1):
        if plus:
            arr[i-1] = i + k
        else:
            arr[i-1] = i -k

        if i % k == 0:
            if plus:
                plus = False
            else:
                plus = True

    return arr

        # below code also works (Backtracking)
# def absolutePermutation(n, k):
#     if k == 0:
#         return [i for i in range(1, n+1)]
#     elif 2*k > n:
#         return [-1]
#
#     arr = [0]*n
#     d = {i:0 for i in range(1, n+1)}
#     for i in range(1, k+1):
#         if d[i+k]:
#             return [-1]
#         d[i+k] = i
#         arr[i-1] = i+k
#     for j in range(n-k+1, n+1):
#         if d[j-k]:
#             return [-1]
#         d[j-k] = j
#         arr[j-1] = j-k
#
#     checked = [0] * n
#     i = k # idx based on 0
#     backtracked = False
#     while i < k + (n-2*k):
#         # not assigned(0)
#         if not arr[i] and not backtracked:
#             if not d[i+1+k]:
#                 d[i+1+k] = i
#                 checked[i] = 1
#                 arr[i] = i+1+k
#                 i += 1
#             elif not d[i+1-k]:
#                 d[i+1-k] = i
#                 checked[i] = 1
#                 arr[i] = i+1-k
#                 i += 1
#             else:
#                 backtracked = True
#                 i -= 1
#         # alr assigned
#         if backtracked:
#             if i == k - 1:
#                 return [-1]
#             if arr[i] == i+1+k:
#                 if d[i+1-k] or checked[i] == -1:
#                     d[arr[i]] = 0
#                     arr[i] = 0
#                     i -= 1
#                     continue
#                 d[arr[i]] = 0
#                 arr[i] = i+1-k
#                 d[i+1-k] = i+1
#                 checked[i] = 1
#                 for j in range(i+1, n):
#                     if checked[j] == 0:
#                         break
#                     checked[j] = 0
#                 backtracked = False
#                 i += 1
#             elif arr[i] == i+1-k:
#                 if d[i+1+k] or checked[i] == 1:
#                     d[arr[i]] = 0
#                     arr[i] = 0
#                     i -= 1
#                     continue
#                 d[arr[i]] = 0
#                 arr[i] = i+1+k
#                 d[i+1+k] = i+1
#                 checked[i] = -1
#                 for j in range(i+1, n):
#                     if checked[j] == 0:
#                         break
#                     checked[j] = 0
#                 backtracked = False
#                 i += 1
#
#     return arr

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(absolutePermutation(n, k))
#
# print(absolutePermutation(100, 2))