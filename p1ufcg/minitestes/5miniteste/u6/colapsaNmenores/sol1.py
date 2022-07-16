def encontrar_menor(lista_numeros):
    menor = lista_numeros[0]
    indice_menor = 0
    for indice in range(1, len(lista_numeros)):
        if menor > lista_numeros[indice]:
            menor = lista_numeros[indice]
            indice_menor = indice
    
    lista_numeros.pop(indice_menor)
    return menor

def colapsa_n_menores(N, nums):
    soma_menores = 0
    for k in range(N):
        menor = encontrar_menor(nums)
        soma_menores += menor
    
    nums.append(soma_menores)

