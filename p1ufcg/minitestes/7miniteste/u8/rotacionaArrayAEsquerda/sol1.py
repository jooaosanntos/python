def rotesq(array):
    if len(array) != 0:
        inicio = array[0]
    for indice in range(len(array) - 1):
        array[indice] = array[indice + 1]
    if len(array) != 0:
        array[len(array) - 1] = inicio
    return array


