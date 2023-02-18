n = int(input())
swifts = []
semaphores = []
swiftstotal = 0
semaphorestotal = 0
counter = 0
largest = 0

games = input().split()
for i in games:
    swifts.append(int(i))
games = input().split()
for i in games:
    semaphores.append(int(i))

for k in range(n):
    swiftstotal += swifts[k]
    semaphorestotal += semaphores[k]

    if semaphorestotal == swiftstotal:
        largest = k+1
    else:
        counter += 1

if counter==n:
    print("0")
else:
    print(largest)