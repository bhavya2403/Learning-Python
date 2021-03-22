N = int(input())
arr = []
for N_itr in range(N):
    firstNameEmailID = input().split()

    firstName = firstNameEmailID[0]

    emailID = firstNameEmailID[1]

    if emailID.endswith("@gmail.com"):
        arr.append(firstName)

for names in sorted(arr):
    print(names)