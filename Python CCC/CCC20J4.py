#CCC 2020 J4 - Cyclic Shifts

text = input()
shift = input()
counter = 0

if shift in text:
    counter += 1

for x in range(len(shift)):
    shift = list(shift)
    
    temp = shift[0]
    shift.append(temp)
    shift.pop(0)

    shift = ''.join(shift)

    if shift in text:
        counter += 1
        break

if counter >= 1:
    print("yes")
else:
    print("no")