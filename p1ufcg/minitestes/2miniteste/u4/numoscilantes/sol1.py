strvalor = input()

ctt = 0
rsp = 0

for k in strvalor:
    ctt += 1

for i in range(len(strvalor)):
    valorint = int(strvalor[i])
    if i == 0:
        if valorint % 2 == 0:
            rsp = 0
        else:
            rsp = 1
        continue
    if rsp == 0  and valorint % 2 == 0:
        rsp = -1
        break
    elif rsp == 1 and valorint % 2 != 0:
        rsp = -1
        break
    else:
        if rsp == 0:
            rsp = 1
        else:
            rsp = 0

if rsp == -1:
    print(f"falso: {ctt} algarismos.")
else:
    print(f"verdadeiro: {ctt} algarismos.")
