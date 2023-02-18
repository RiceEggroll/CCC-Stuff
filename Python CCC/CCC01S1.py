#do this better
cards = input()
points = 0
cardnum = 0
suite = 0
drawn = ""

total = 0

print("Cards Dealt\tPoints")

for i in cards[1:]:
    if i == "D" or i == "H" or i == "S" :
        if cardnum == 0:
            points += 3
        if cardnum == 1:
            points += 2
        if cardnum == 2:
            points += 1

        if suite == 0:
            print("Clubs "+drawn+"\t" + str(points))
        if suite == 1:
            print("Diamonds "+drawn+"\t" + str(points))
        if suite == 2:
            print("Heart "+drawn+"\t" + str(points))
        
        total += points
        suite += 1
        points = 0
        cardnum = 0
        drawn = ""
        continue

    drawn += i +" "

    if i == "A":
        points += 4
    if i == "K":
        points += 3
    if i == "Q":
        points += 2
    if i == "J":
        points += 1
    cardnum += 1

print("Spades "+drawn+"\t" + str(points))
total += points

print("\t\tTotal "+str(total))