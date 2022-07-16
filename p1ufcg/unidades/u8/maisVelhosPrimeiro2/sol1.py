def idosos_inicio(fila):
    posicao_idosos = 0

    for indice in range(len(fila)):
        if fila[indice] >= 60:
            fila[indice], fila[posicao_idosos] = fila[posicao_idosos], fila[indice]
            posicao_idosos += 1


