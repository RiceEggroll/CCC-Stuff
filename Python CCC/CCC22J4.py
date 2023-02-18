#TLE'd so optimize it fatass

x = int(input())
together = []
for i in range(x):
    together.append(input().split())

y = int(input())
seperate = []
for i in range(y):
    seperate.append(input().split())

z = int(input())
groups = []
for i in range(z):
    groups.append(input().split())

counter=0

for a in range(x):
    for b in range(z):
        if together[a][0] in groups[b] or together[a][0] in groups[b]:
            if together[a][0] and together[a][1] not in groups[b]:
                counter += 1
                break

for a in range(y):
    for b in range(z):
        if seperate[a][0] in groups[b]:
            if seperate[a][1] in groups[b]:
                counter += 1
                break

print(counter)