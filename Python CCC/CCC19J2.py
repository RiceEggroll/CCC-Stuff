#CCC 2019 J2 - Time to Decompress

l = int(input())
message = []

for x in range(l):
    message = input().split(" ")
    n = int(message[0])
    
    for i in range(n-1):
        print(message[1],end = "")
    print(message[1])