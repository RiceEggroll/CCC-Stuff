numbers = []

for x in range(4):
    numbers.append(int(input()))

if (numbers[0] == 8 or numbers[0] == 9) and (numbers [1] == numbers[2]) and (numbers[-1] == 8 or numbers[-1] == 9):
    print("ignore")
else:
    print("answer")