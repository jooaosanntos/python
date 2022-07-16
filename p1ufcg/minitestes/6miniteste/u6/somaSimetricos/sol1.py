def soma_simetricos(valores):
    lista_soma = []

    indice_inicial = 0
    indice_final = len(valores) - 1
    while True:
        if indice_inicial > indice_final: break
        elif indice_inicial == indice_final:
            lista_soma.append(valores[indice_inicial])
        else:
            lista_soma.append(valores[indice_inicial] + valores[indice_final])

        indice_inicial += 1
        indice_final -= 1

    return lista_soma

