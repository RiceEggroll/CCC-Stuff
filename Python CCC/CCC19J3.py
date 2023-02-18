#CCC 2019 J3 - Cold Compress

n = int(input())

for x in range(n):
    message = list(input())
    counter = 0
    char = " "
    encoded = ""
    for i in range(len(message)):
        if message[i] != char and counter != 0:
            encoded += str(counter) +  " "
            encoded += char + " "
            counter = 1
        else:
            counter += 1
        char = message[i]
    if counter != 0:
        encoded += str(counter) + " "
        encoded += char
    print(encoded)