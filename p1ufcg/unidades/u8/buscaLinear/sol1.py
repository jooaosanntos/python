def busca(seq, valor):
    for indice in range(len(seq)):
        if valor == seq[indice]:
            return indice
    return -1

