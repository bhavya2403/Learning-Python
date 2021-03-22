bhavya_file = open("bhavya.txt", "r")
print(bhavya_file.readable())

for lines in bhavya_file:
    print(lines)

print(bhavya_file.readlines())

print(bhavya_file.readline())
# we can read the lines in file only once
bhavya_file.close()

bhavya_file = open("bhavya.txt", "a")
# a=append. add another line at last
bhavya_file.write("bhavya")
# do not run file twice it'll write same text again which is permanent
bhavya_file.write("\nBHAVYA")
bhavya_file.close()

bhavya_file1 = open("bhavya1.txt", "w")
# we can make a new file as well from here
# delete last info in file and overwrite
bhavya_file1.write("bhavya")
bhavya_file1.close()


