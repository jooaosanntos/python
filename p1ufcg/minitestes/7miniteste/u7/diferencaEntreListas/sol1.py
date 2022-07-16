def diferenca_listas(lista1, lista2):
    for indice1 in range(len(lista1) - 1, -1, -1):
        
        for indice2 in range(len(lista2) - 1, -1, -1):
            print(lista1[indice1], lista2[indice2])
            if lista1[indice1] == lista2[indice2]:

                lista1.pop(indice1)
                lista2.pop(indice2) 
                break

    return lista1

    
