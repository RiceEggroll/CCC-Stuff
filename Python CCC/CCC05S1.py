#CCC 2005 S1 - Snow Calls

repeat = int(input())
phone = ""

for a in range(repeat):
    phone = ""
    number = list(input())

# Code I found online to remove the hyphens
#    try:
#        while True:
#            number.remove("-")
#    except ValueError:
#        pass

    while "-" in number:
        number.remove("-")

    while len(number) > 10:
        number.pop(-1)

    for i in range(len(number)):
        if number[i] == "A" or number[i] == "B" or number[i] == "C":
            number[i] = "2"
        if number[i] == "D" or number[i] == "E" or number[i] == "F":
            number[i] = "3"
        if number[i] == "G" or number[i] == "H" or number[i] == "I":
            number[i] = "4"
        if number[i] == "J" or number[i] == "K" or number[i] == "L":
            number[i] = "5"
        if number[i] == "M" or number[i] == "N" or number[i] == "O":
            number[i] = "6"
        if number[i] == "P" or number[i] == "Q" or number[i] == "R" or number[i] == "S":
            number[i] = "7"
        if number[i] == "T" or number[i] == "U" or number[i] == "V":
            number[i] = "8"
        if number[i] == "W" or number[i] == "X" or number[i] == "Y" or number[i] == "Z":
            number[i] = "9"

    for x in range(3):
        phone = phone + str(number[x])
    phone = phone + "-"
    for x in range(3):
        phone = phone + str(number[x+3])
    phone = phone + "-"
    for x in range(4):
        phone = phone + str(number[x+6])

    print(phone)