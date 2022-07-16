string1 = input()
string2 = input()

saida = ""
notfound = True
for index2 in range(len(string2)):
    for index1 in range(len(string1)):
        if string1[index1] == string2[index2]:
            saida += f"{index1}"
            notfound = False
    if notfound:
        saida += "N"
    notfound = True
    saida += "Q"

for index in range(len(saida) - 1):
    if saida[index] == "Q": continue
    
    if saida[index] == "N":
        print("-1")
    elif saida[index + 1] != "Q":
        print(saida[index], end=" ")
    else:
        print(saida[index])
