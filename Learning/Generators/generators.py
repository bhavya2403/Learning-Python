def fibonachi(k):
    ary = [0, 1]
    count = 2
    while count < k:
        number = ary[len(ary) - 1] + ary[len(ary) - 2]
        ary.append(number)
        count += 1
    return ary


print(fibonachi(10))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for f in fib():
    if f > 35:
        break
    print(f)
# difference between yield and return is: return destroys all the local variables and just return the asked value.
# but yield preserves the state of last execution.
# yield has a benefit of saving memory and quick processing
