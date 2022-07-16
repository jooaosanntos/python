from p1 import Array
from random import randint

arr = Array(10)
for indice1 in range(10):
    arr[indice1] = randint(0, 9)
print(arr)


def ordenar_elemento(arr, indice_final):
    for indice in range(indice_final, 0, -1):
        if arr[indice - 1] > arr[indice]:
            arr[indice - 1], arr[indice] = arr[indice], arr[indice - 1]
        else: return


for indice2 in range(1, len(arr)):
    ordenar_elemento(arr, indice2)

print(arr)

