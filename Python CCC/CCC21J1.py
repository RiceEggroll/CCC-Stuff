#CCC 2021 J1 - Boiling Point

b = int(input())

p = 5*b-400

print(p)

if p > 100:
    print("-1")
elif p == 100:
    print("0")
else:
    print("1")