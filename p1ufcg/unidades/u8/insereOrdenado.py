from p1 import Array


def mover_direita(arr, posicao):
    for indice in range(len(arr) - 1, posicao, -1):
        arr[indice] = arr[indice - 1]


def encontrar_posicao(arr, valor):
    for indice in range(len(arr)):
        if arr[indice] == None: 
            arr[indice] = valor
            break
        if arr[indice] > valor:
            mover_direita(arr, indice)
            arr[indice] = valor
            break


arr = Array(5)
while True:
    entrada = int(input("valor? "))
    if entrada == -1: break

    encontrar_posicao(arr, entrada)

    print(arr)
