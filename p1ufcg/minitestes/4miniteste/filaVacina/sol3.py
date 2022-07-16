correto = 0
errado = 0

while True:
    fila_vacina = input()
    if fila_vacina == '###': break

    index = 1
    muda = False
    while index != len(fila_vacina):
        if (fila_vacina[index] == 'c' or fila_vacina[index] == 'i') and fila_vacina[index - 1] == 'a':
            muda = True
            errado += 1
            break
        index += 1
    if muda == False:
        correto += 1
print(f'sim: {correto}\nnão: {errado}')
