n = int(input())
score = 0
fouls = 0
counter = 0

for i in range(n):
    score = int(input())
    fouls = int(input())

    total = score*5 - fouls*3
    if total > 40:
        counter += 1

if counter == n:
    print(str(counter)+"+")
else:
    print(counter)