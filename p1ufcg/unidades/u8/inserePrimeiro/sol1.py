def insere_ordenado_primeiro(l1):
    for indice in range(len(l1) - 1):
        if l1[indice] > l1[indice + 1]:
            l1[indice], l1[indice + 1] = l1[indice + 1], l1[indice]
        else: return

