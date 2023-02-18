#CCC 2014 J2 - Vote Count

v = int(input())
votes = list(input())
acounter = 0
bcounter = 0

for i in votes:
    if i == "A":
        acounter += 1
    else:
        bcounter += 1

if acounter > bcounter:
    print("A")
elif bcounter > acounter:
    print("B")
else:
    print("Tie")