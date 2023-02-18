#CCC 2011 S1 - English or French?

tcounter = 0
scounter = 0

n = int(input())

for x in range(n):
    passage = input()
    passage = list(passage)

    for i in passage:
        if i == "T" or i == "t":
            tcounter += 1
        if i == "S" or i == "s":
            scounter += 1
    
if scounter > tcounter or scounter == tcounter:
    print("French")

if tcounter > scounter:
    print("English")