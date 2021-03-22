from typing import List, Union

friends = ["kathan", "dharmil", "supan", "darshil"]
print(friends[0])
print(friends[1:3])
friends[0] = "shrey"
print(friends)

luckey_numbers = [24, 3, 2003]
friends.extend(luckey_numbers)
print(friends)

friends.remove(24)
friends.remove(3)
friends.remove(2003)
print(friends)

friends.append("bhavya")
print(friends)

friends.insert(2, "bhavya")
print(friends)

friends.remove("supan")
print(friends)

friends.pop()
print(friends)

print(friends.index("dharmil"))

friends.append("bhavya")
print(friends)

print(friends.count("bhavya"))

friends.sort()
print(friends)

luckey_numbers.sort()
print(luckey_numbers)

friends.reverse()
print(friends)

friends1 = friends.copy()
print(friends1)
