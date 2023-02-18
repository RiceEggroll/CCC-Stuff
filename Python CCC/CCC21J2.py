#CCC 2021 J2 - Silent Auction

n = int(input())
bidders = []
amounts = []
highestbid = 0
winner = ""

for x in range(n):
    bidder = input()
    amount = int(input())

    bidders.append(bidder)
    amounts.append(amount)

for i in range(n):
    if amounts[i] > highestbid:
        highestbid = amounts[i]
        winner = bidders[i]
    if amounts[i] == highestbid:
        continue

print(winner)