def gera_lista_frequencias(lista):
    lista_frequencias = [0,0,0,0,0,0,0,0,0,0]
    for indice in range(len(lista)):
        lista_frequencias[lista[indice]] += 1
    return lista_frequencias

def remover_elementos(elemento, lista, vezes):
    for rep in range(vezes):
        for indice_lista in range(len(lista)):
            if lista[indice_lista] == elemento:
                lista.pop(indice_lista)
                break

def remove_muitas_ocorrencias(lista):
    lista_frequencias = gera_lista_frequencias(lista)

    for indice in range(len(lista_frequencias)):
        if lista_frequencias[indice] >= 3:
            remover_elementos(indice, lista, lista_frequencias[indice])

