def matriz_menor(M1, M2):
    matriz_menor = M1

    for indice_linha in range(len(M1)):
        
        for indice_coluna in range(len(M1[indice_linha])):
            menor = 0
            if M1[indice_linha][indice_coluna] > M2[indice_linha][indice_coluna]:
                menor = M2[indice_linha][indice_coluna]
            else:
                menor = M1[indice_linha][indice_coluna]

            matriz_menor[indice_linha][indice_coluna] = menor


    return matriz_menor

