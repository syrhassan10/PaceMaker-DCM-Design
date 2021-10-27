f = open("User_data.txt", 'r')
username = "syrhassan10"
print(f.readlines())

for line in f:
    temp = line.split(" ")
    if username == temp[0]:
        print('name unavulable')