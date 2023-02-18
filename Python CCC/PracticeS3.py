#incomplete 

n = int(input())
r = []

for x in range(n):
    r.append(int(input()))
r.sort()

previous = r[0]
highest = 0
counter = 0
frequent = max(r)

for i in r:
    if i == previous:
        counter+=1
    
    if i != previous:
        if counter >= highest:
            highest = counter
            frequent = previous
        counter = 1
        previous = i
if counter >= highest:
    highest = counter
    frequent = previous

while frequent in r:
    r.remove(frequent)

previous = r[0]
highest = 0
counter = 0
sfrequent = min(r)

for i in r:
    if i == previous:
        counter+=1
    
    if i != previous:
        if counter > highest:
            highest = counter
            sfrequent = previous
        counter = 1
        previous = i
if counter > highest:
    highest = counter
    sfrequent = previous
if counter == highest:
    if abs(frequent - sfrequent) > abs(frequent - i):
        highest = counter


if highest == 1:
    diff = 0
    for x in range(len(r)):
        if abs(frequent - r[x]) >= diff:
            diff = abs(frequent - r[x])
else:
    diff = abs(frequent - sfrequent)
print(diff)