string = input()

coded_string = ""
ctt = 0

for i in range(len(string)):
    if i == 0:
        coded_string = coded_string + string[i]
        continue
    if string[i] == "a" or string[i] == "A":
        coded_string = coded_string + "4"
        ctt += 1
    elif string[i] == "e" or string[i] == "E":
        coded_string = coded_string + "3"
        ctt += 1
    elif string[i] == "i" or string[i] == "I":
        coded_string = coded_string + "1"
        ctt += 1
    elif string[i] == "o" or string[i] == "O":
        coded_string = coded_string + "0"
        ctt += 1
    else:
        coded_string = coded_string + string[i]

print(f"{coded_string} ({ctt} troca(s))")
