def bubblesort(dados):
    while True:
        trocou = False
        for indice in range(len(dados) - 1):
            if dados[indice] > dados[indice + 1]:
                dados[indice], dados[indice + 1] = dados[indice + 1], dados[indice]
                trocou = True
        if not trocou: return dados

