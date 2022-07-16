lista_postos = []
while True:
    entrada = input()
    
    if entrada == "###": break
    
    lista_postos.append(entrada)


achou_adulto = False
qtd_irregular = 0

ctt = 0
while ctt < len(lista_postos):
    ctt2 = 0
    while ctt2 < len(lista_postos[ctt]):
        if lista_postos[ctt][ctt2] == "a":
            achou_adulto = True
        if achou_adulto and (lista_postos[ctt][ctt2] == "i" or lista_postos[ctt][ctt2] == "c"):
            qtd_irregular += 1
            break
        ctt2 += 1
    achou_adulto = False
    ctt += 1

qtd_regular = len(lista_postos) - qtd_irregular

print(f"sim: {qtd_regular}")
print(f"não: {qtd_irregular}")
