#CCC 2006 J2 - Roll the Dice

counter = 0
first = int(input())
second = int(input())

for x in range(first):
    x += 1
    for i in range(second):
        i += 1
        if i + x == 10:
            counter += 1

if counter == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are "+str(counter)+" ways to get the sum 10.")