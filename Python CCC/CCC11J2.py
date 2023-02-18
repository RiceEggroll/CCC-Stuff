#CCC 2011 J2 - Who Has Seen The Wind?

humidity = int(input())
max = int(input())
counter = 0
time = 0

for t in range(max):
    if counter == 2:
        break
    height = ((-6*(t**4))+(humidity*(t**3))+(2*(t**2))+t)
    if height <= 0:
        counter += 1
        time = t

if time == 0:
    print("The balloon does not touch ground in the given time.")
elif time > 0:
    print("The balloon first touches ground at hour:")
    print(t-1)