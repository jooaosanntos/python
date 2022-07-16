def encontra_menores(numero, lista):
    for elemento in lista:
        if elemento < numero:
            return elemento
    return -1

