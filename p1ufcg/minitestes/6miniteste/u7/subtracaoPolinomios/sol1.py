def complementar_menor(menor, vezes):
    for indice in range(vezes):
        menor.append(0)

def remover_zeros(lista):
    nao_zero = False
    for indice in range(len(lista) - 1, -1, -1):
        if nao_zero: break
        if lista[indice] == 0:
            lista.pop(indice)
        else:
            nao_zero = True

def subtrai_polinomios(p1, p2):
    if len(p1) > len(p2):
        complementar_menor(p2, len(p1), - len(p2))
    elif len(p1) < len(p2):
        complementar_menor(p1, len(p2) - len(p1))
    
    poli_final = []
    for indice in range(len(p1)):
        poli_final.append(p1[indice] - p2[indice])

    remover_zeros(poli_final)

    return poli_final

p1 = [1,2,3]
p2 = [2,3,3]

print(subtrai_polinomios(p1, p2))

