arr_valores = input().split(" ")

ant = ""
ctt = 0

for i in range(len(arr_valores)):
    if i == 0:
        ant = arr_valores[0]
    else:
        if ant == arr_valores[i]:
            ctt += 1
            ant = arr_valores[i]
        else:
            ant = arr_valores[i]

print(ctt)
