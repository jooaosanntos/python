def remove_all1(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            lista.pop(i)
            return remove_all1(lista, elemento)

def remove_all2(lista, elemento):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)

lista = [1,2,3,2,2]

remove_all1(lista, 2)
print(lista)

lista2 = [1,2,3,2,2]
remove_all2(lista, 2)
print(lista)
