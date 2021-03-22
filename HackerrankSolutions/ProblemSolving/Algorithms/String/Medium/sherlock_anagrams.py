# def sherlockAndAnagrams(s): # O(n3log(n))
#     d = {}
#     count = 0
#     size = len(s)
#     for i in range(1, size):
#         for j in range(size-i+1):
#             s1 = str(sorted(s[j:j+i].strip()))
#             if s1 not in d:
#                 d[s1] = 1
#             else:
#                 count += d[s1]
#                 d[s1] += 1
#         d = {}
#     return count
def sherlockAndAnagrams(s): # O(n3)
    signature = {}
    count = 0
    size = len(s)
    for i in range(1, size):
        for j in range(size - i + 1):
            sign = [0] * 26
            for k in s[j:j + i]:
                sign[ord(k) - 97] += 1
            str_sign = str(sign)
            if str_sign not in signature:
                signature[str_sign] = 1
            else:
                count += signature[str_sign]
                signature[str_sign] += 1
        signature = {}
    return count


print(sherlockAndAnagrams('kkkk'))