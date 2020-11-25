Sum = 0
for i in range(1, 100):
    if i % 2 == 1:
        Sum += i
print(Sum)

sum1 = 0
for i in range(1, 100):
    if i % 2 == 0:
        sum1 += i
print(sum1)

sum2 = 0
i = 1
while i < 10:
    sum2 += i
    i += 2
print(sum2)

for tracker in "bring":
    if tracker == "i":
        print(tracker)
        print("The End")
        break
