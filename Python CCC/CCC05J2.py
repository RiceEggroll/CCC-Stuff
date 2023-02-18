#CCC 2005 J2 - RSA Numbers

first = int(input())
second = int(input())
counter = 0

for x in range(first, second+1):
    dcounter = 0

    for i in range(1,x+1):
        if (x % i) == 0:
            dcounter += 2

    if dcounter == 4:
        counter += 1

print("The number of RSA numbers between "+str(first)+" and "+str(second)+" is "+str(counter))