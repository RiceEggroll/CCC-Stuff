#CCC 2000 J2 - 9966

flip = [0,1,8,11,69,88,96,111,6699,9966,8008]
start = (int(input()))
end = (int(input()))
rotation = 0

for start in range(end):
    start+1
    if start in flip:
        rotation += 1

print(rotation)