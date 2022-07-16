def idosos_inicio(fila):
    while True:
        trocou = False
        for indice in range(len(fila) - 1):
            if (fila[indice] < fila[indice  + 1] and fila[indice] < 60 and fila[indice + 1] >= 60):
                fila[indice], fila[indice + 1] = fila[indice + 1], fila[indice]
                trocou = True
        if not trocou: return

fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
print(fila)
