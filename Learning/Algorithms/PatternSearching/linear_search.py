from util import time_it

@time_it
def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i

    return 'Value Not Found'


print(linear_search([i for i in range(10000001)], 10000000))  # took 620ms
