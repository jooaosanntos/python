def ultimo_indice(num, lista):
    ultimo_indice = -1
    for indice in range(len(lista)):
        if lista[indice] == num:
            ultimo_indice = indice
    return ultimo_indice

