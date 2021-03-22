def solve(S, sum_arr, sumOfSubset):
    d = {}
    alr_taken = [False] * len(S)
    count = 0
    for i in S:
        d[i] = count
        count += 1

    for i in S:
        if i+sum(sum_arr) < sumOfSubset and not alr_taken[d[i]]: # this is the bounding function in the state space tree
            # set is not changing size during iteration either the function will return or in case of fail
            # we are already adding the same node
            sum_arr.append(i)
            S.remove(i)
            alr_taken[d[i]] = True

            if solve(S, sum_arr, sumOfSubset):
                return True

            S.add(sum_arr.pop()) # means condition is false and now we are killing that node

        elif i+sum(sum_arr) == sumOfSubset:
            sum_arr.append(i)
            return True

    return False

def sumSubsets(S, sumOfSubset):
    sum_arr = []
    if solve(S, sum_arr, sumOfSubset):
        return sum_arr
    return 'Not Possible'


print(sumSubsets({5,10,12,13,15,18}, 33))
# 18,5,10,12,13,15
