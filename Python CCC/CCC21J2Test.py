n = int(input())
highest = 0
winner = ""

for i in range(n):
    current = input()
    currentAmount = int(input())

    if currentAmount > highest :
        highest = currentAmount
        winner = current

print(winner)