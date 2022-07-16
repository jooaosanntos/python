lista_postos = []
while True:
    entrada = input()
    
    if entrada == "###": break
    
    lista_postos.append(entrada)


achou_adulto = False
qtd_irregular = 0
for posto in lista_postos:
    for pessoa in posto:
        if pessoa == "a":
            achou_adulto = True
        if achou_adulto and (pessoa == "i" or pessoa == "c"):
            qtd_irregular += 1
            break
    achou_adulto = False

qtd_regular = len(lista_postos) - qtd_irregular

print(f"sim: {qtd_regular}")
print(f"não: {qtd_irregular}")
