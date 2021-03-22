numbers = [1, 2, 5, 10, 6, 5, 5, 10]
remove_dupl = set(numbers)
remove_dupl = list(numbers)
print(remove_dupl)

x = {"a", "b", "c"}
x.add("d")
x.add("e")
print(x)
print("a" in x)
for i in x:
    print(i)

y = frozenset({"a", "f", "g"})
# y.add(11) will not work here

print(x | y)
print(x & y)
print(x - y)
print(x < y)
