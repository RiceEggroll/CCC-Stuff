tune = input()
tune = list(tune)
cmd = []
output = ""
numbers = ["0","1","2","3","4","5","6","7","8","9"]

tune.append("p")
for x in range(len(tune)):
    if tune[x] not in numbers:
        cmd.append(tune[x])
    if tune[x] in numbers:
        if tune[x+1] not in numbers:
            cmd.append(tune[x])
            for i in range(len(cmd)):
                if cmd[i] == "+":
                    output += " tighten "
                if cmd[i] == "-":
                    output += " loosen "
                if cmd[i] != "+" and cmd[i] != "-":
                    output += cmd[i]
            print(output)
            output = ""
            cmd = []
        else:
            cmd.append(tune[x])