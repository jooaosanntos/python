from p1 import Array

def blefe(lista):
    lista_diferencas = Array(len(lista))
    if len(lista_diferencas) != 0:
        lista_diferencas[0] = 0
    for indice in range(1, len(lista)):
        if lista[indice] > lista[indice - 1]:
            diferenca = lista[indice] - lista[indice - 1]
            lista[indice] = lista[indice - 1]
            lista_diferencas[indice] = diferenca
        else:
            lista_diferencas[indice] = 0

    return lista_diferencas

