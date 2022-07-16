def maior_sublista(sublistas):
    maior = len(sublistas[0])
    maior_lista = sublistas[0]
    for lista in sublistas:
        if len(lista) > maior:
            maior = len(lista)
            maior_lista = lista

    return maior_lista

def meu_reverse(lista):
    lista_final = []
    for i in range(len(lista) - 1, -1, -1):
        lista_final.append(lista[i])

    return lista_final

def maior_slice(lista):
    sublista = []
    indice_sublista = 0
    aberto = False
    for indice in range(len(lista) - 1, -1, -1):
        if lista[indice] > lista[indice - 1]:
            if len(sublista) == 0:
                sublista.append([lista[indice]])
                aberto = True
                continue
            else:
                if aberto:
                    sublista[indice_sublista].append(lista[indice])
                else:
                    sublista.append([lista[indice]])
                    indice_sublista += 1
                    aberto = True
        else:
            if aberto:
                sublista[indice_sublista].append(lista[indice])
                aberto = False

    maior_lista = meu_reverse(maior_sublista(sublista))

    return maior_lista 

